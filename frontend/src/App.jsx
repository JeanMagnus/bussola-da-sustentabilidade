import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { v4 as uuidv4 } from "uuid";
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

const DEFAULT_API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

const THINKING_STEPS = [
  "Entendendo sua pergunta",
  "Consultando a base de dados",
  "Organizando os indicadores relevantes",
  "Montando uma resposta clara para você",
];

function normalizeContent(content) {
  if (typeof content === "string") return content;
  if (Array.isArray(content)) {
    return content
      .map((item) => {
        if (typeof item === "string") return item;
        if (item?.text) return item.text;
        return "";
      })
      .join("\n");
  }
  return "";
}

function useStreamChat({ apiUrl, threadId, userId }) {
  const [messages, setMessages] = useState([]);
  const [isStreaming, setIsStreaming] = useState(false);
  const [error, setError] = useState("");
  const abortRef = useRef(null);

  const sendMessage = useCallback(
    async (text) => {
      if (!text.trim() || isStreaming) return;

      const userMessage = { id: uuidv4(), role: "user", content: text };
      const assistantId = `assistant-${threadId}-${Date.now()}`;

      setMessages((prev) => [
        ...prev,
        userMessage,
        { id: assistantId, role: "assistant", content: "", thinking: "" },
      ]);
      setError("");
      setIsStreaming(true);

      const controller = new AbortController();
      abortRef.current = controller;

      try {
        const response = await fetch(`${apiUrl}/chat/stream`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            message: text,
            thread_id: threadId,
            user_id: userId,
          }),
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        const reader = response.body?.getReader();
        if (!reader) throw new Error("Não foi possível iniciar o stream da resposta.");

        const decoder = new TextDecoder();
        let buffer = "";

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });
          const lines = buffer.split("\n");
          buffer = lines.pop() ?? "";

          for (const line of lines) {
            const cleaned = line.trim();
            if (!cleaned.startsWith("data:")) continue;

            const payload = cleaned.replace(/^data:\s*/, "");
            if (!payload) continue;

            try {
              const parsed = JSON.parse(payload);
              const { event, data } = parsed;

              // if ((event === "messages/partial" || event === "messages/complete") && Array.isArray(data)) {
              //   const streamed = normalizeContent(data[0]?.content);
              //   setMessages((prev) =>
              //     prev.map((msg) => (msg.id === assistantId ? { ...msg, content: streamed } : msg)),
              //   );
              // }

              if (event == "chunk" && data?.content) {
                setMessages((prev) =>
                  prev.map((msg) =>
                    msg.id === assistantId
                      ? { ...msg, content: msg.content + data.content}
                      : msg
                  )
                );
              }

              if (event == "thinking" && data?.content) {
                setMessages((prev) =>
                  prev.map((msg) =>
                    msg.id === assistantId
                      ? { ...msg, thinking: (msg.thinking || "") + data.content }
                      : msg
                  )
                );
              }

              if (event === "status" && data?.message) {
                setMessages((prev) =>
                  prev.map((msg) =>
                    msg.id === assistantId
                      ? { 
                          ...msg, 
                          // Adiciona o status da ferramenta ao balão de raciocínio
                          thinking: (msg.thinking || "") + `\n⚙️ *${data.message}*\n` 
                        }
                      : msg
                  )
                );
              }

              if (event === "messages/complete") {
              }

              if (event === "error") {
                setError(data?.message ?? "Erro ao processar resposta do servidor.");
              }
            } catch {
              // payload inválido
            }
          }
        }
      } catch (err) {
        if (err.name !== "AbortError") {
          setError(err.message || "Erro inesperado.");
        }
      } finally {
        setIsStreaming(false);
        abortRef.current = null;
      }
    },
    [apiUrl, isStreaming, threadId, userId],
  );

  const stopStream = useCallback(() => abortRef.current?.abort(), []);

  return {
    messages,
    error,
    isStreaming,
    sendMessage,
    stopStream,
    clearChat: () => {
      setMessages([]);
      setError("");
    },
  };
}

function Message({ role, content, thinking }) {
  const isUser = role === "user";

  return (
    <div className={`message-row ${isUser ? "is-user" : ""}`}>
      <article className={`message-bubble ${isUser ? "is-user" : "is-assistant"}`}>

        {!isUser && thinking && (
          <details className="thinking-details">
            <summary className="thinking-summary">
              🧠 O agente pensou...
            </summary>

            <div className="thinking-content">
              {thinking}
            </div>
          </details>
        )}

        {content ? (
          <ReactMarkdown remarkPlugins={[remarkGfm]}>
            {content}
          </ReactMarkdown>
        ) : (
          !isUser && (
            <div className="typing-container">
              <div className="loading-spinner"></div>
              <span className="loading-text">
                {thinking ? "A finalizar a análise..." : "A iniciar processo..."}
              </span>
            </div>
          )
        )}

      </article>
    </div>
  );
}


function ThinkingTimeline({ isVisible }) {
  const [activeStep, setActiveStep] = useState(0);

  useEffect(() => {
    if (!isVisible) {
      setActiveStep(0);
      return;
    }

    const interval = setInterval(() => {
      setActiveStep((prev) => Math.min(prev + 1, THINKING_STEPS.length - 1));
    }, 1100);

    return () => clearInterval(interval);
  }, [isVisible]);

  if (!isVisible) return null;

  return (
    <section className="thinking-panel" aria-live="polite">
      <div className="thinking-title">O agente está processando sua pergunta</div>
      <ul>
        {THINKING_STEPS.map((step, index) => (
          <li 
            key={step} 
            className={`
              ${index <= activeStep ? "active" : ""} 
              ${index === activeStep ? "blinking" : ""}
            `}
          >
            <span className="step-dot" />
            <span>{step}</span>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default function App() {
  const [input, setInput] = useState("");
  const [threadId] = useState(() => uuidv4());
  const bottomRef = useRef(null);
  const textareaRef = useRef(null);

  const [theme, setTheme] = useState("light");
    function toggleTheme() {
    setTheme((currentTheme) =>
      currentTheme === "dark" ? "light" : "dark"
    );
  }

  const { messages, error, isStreaming, sendMessage, stopStream, clearChat } = useStreamChat({
    apiUrl: DEFAULT_API_URL,
    threadId,
    userId: "web-user",
  });

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isStreaming]);

  useEffect(() => {
    if (!textareaRef.current) return;
    textareaRef.current.style.height = "0px";
    textareaRef.current.style.height = `${Math.min(textareaRef.current.scrollHeight, 180)}px`;
  }, [input]);

  const canSend = useMemo(() => input.trim().length > 0 && !isStreaming, [input, isStreaming]);
  const lastMessage = messages.at(-1);
  const showThinking = isStreaming && lastMessage?.role === "assistant" && !lastMessage?.content;

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!canSend) return;
    sendMessage(input.trim());
    setInput("");
  };

  return (
    <div className="app-bg" data-theme={theme}>
      <div className="chat-shell">
        <header className="chat-header">
          <div className="brand">
            <span className="brand-dot" />
            <div>
              <h1>Bússola da Sustentabilidade</h1>
              <p>Assistente de análise de dados </p>
            </div>
          </div>

          <div className="header-actions">
            <button
              type="button"
              className="theme-btn"
              onClick={toggleTheme}
              aria-label="Alternar tema"
            >
              {theme === "dark" ? "Tema claro" : "Tema escuro"}
            </button>
            <button type="button" onClick={clearChat} className="ghost-btn">
            Nova conversa
            </button>
          </div>
        </header>

        <main className="chat-main">
          {messages.length === 0 ? (
            <section className="empty-state">
              <h2>Faça sua primeira pergunta</h2>
              <p>
                Converse com o agente em linguagem natural e receba respostas em tempo real com contexto do
                projeto.
              </p>

              <div className="prompt-list">
                {[
                  "Quais cidades têm melhor indicador geral de sustentabilidade?",
                  "Compare Bombinhas e Urubici em turismo e renda.",
                  "Mostre os principais insights de 2023 para SC.",
                ].map((prompt) => (
                  <button key={prompt} type="button" onClick={() => setInput(prompt)}>
                    {prompt}
                  </button>
                ))}
              </div>
            </section>
          ) : (
            messages.map((msg) => <Message key={msg.id} role={msg.role} content={msg.content} thinking={msg.thinking} />)
          )}

          <ThinkingTimeline isVisible={showThinking} />

          {error && <div className="error-banner">⚠ {error}</div>}
          <div ref={bottomRef} />
        </main>

        <form className="chat-input" onSubmit={handleSubmit}>
          <textarea
            ref={textareaRef}
            value={input}
            onChange={(event) => setInput(event.target.value)}
            placeholder="Digite sua pergunta..."
            rows={1}
            onKeyDown={(event) => {
              if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault();
                handleSubmit(event);
              }
            }}
          />

          <div className="input-actions">
            <span className="hint">Enter envia · Shift + Enter quebra linha</span>
            {isStreaming ? (
              <button type="button" className="stop-btn" onClick={stopStream}>
                Parar
              </button>
            ) : (
              <button type="submit" disabled={!canSend} className="send-btn">
                Enviar
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
}