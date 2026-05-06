import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { v4 as uuidv4 } from "uuid";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { CiCirclePlus } from "react-icons/ci";
import { FiSun, FiMoon } from "react-icons/fi";
import { useStream, FetchStreamTransport } from "@langchain/langgraph-sdk/react";

const DEFAULT_API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

const THINKING_STEPS = [
  "Entendendo sua pergunta",
  "Consultando a base de dados",
  "Organizando os indicadores relevantes",
  "Montando uma resposta clara para você",
];

const EMPTY_MESSAGES = [];
const INITIAL_VALUES = { messages: [] };

function normalizeContent(content) {
  if (typeof content === "string") return content;
  if (Array.isArray(content)) {
    return content.map((item) => (typeof item === "string" ? item : item?.text || "")).join("\n");
  }
  return "";
}

function getMessageRole(msg) {
  if (!msg) return "assistant";
  if (msg.role === "user" || msg.role === "assistant") return msg.role;
  if (msg.type === "human") return "user";
  if (msg.type === "ai" || msg.type === "AIMessageChunk") return "assistant";
  return msg.role ?? msg.type ?? "assistant";
}

function getLastAssistantMessage(messages) {
  return [...messages].reverse().find((msg) => getMessageRole(msg) === "assistant");
}

// function Message({ role, content }) {
//   const isUser = role === "user";
//   return (
//     <div className={`message-row ${isUser ? "is-user" : ""}`}>
//       <article className={`message-bubble ${isUser ? "is-user" : "is-assistant"}`}>
//         {content ? (
//           <ReactMarkdown remarkPlugins={[remarkGfm]}>{normalizeContent(content)}</ReactMarkdown>
//         ) : (
//           !isUser && (
//             <div className="typing-container">
//               <div className="loading-spinner" />
//               <span className="loading-text">Gerando resposta...</span>
//             </div>
//           )
//         )}
//       </article>
//     </div>
//   );
// }

function Message({ role, content }) {
  const isUser = role === "user";

  return (
    <div className={`message-row ${isUser ? "is-user" : "is-assistant"}`}>
      {!isUser && (
        <div className="message-avatar assistant-avatar" aria-hidden="true">
          🧭
        </div>
      )}

      <div className={`message-content ${isUser ? "is-user" : "is-assistant"}`}>
        <span className="message-sender">
          {isUser ? "Você" : "Bússola"}
        </span>

        <article className={`message-bubble ${isUser ? "is-user" : "is-assistant"}`}>
          {content ? (
            <ReactMarkdown remarkPlugins={[remarkGfm]}>
              {normalizeContent(content)}
            </ReactMarkdown>
          ) : (
            !isUser && (
              <div className="typing-container">
                <div className="loading-spinner" />
                <span className="loading-text">Gerando resposta...</span>
              </div>
            )
          )}
        </article>
      </div>
    </div>
  );
}

function LiveProcessing({ thinking, isStreaming }) {
  if (!isStreaming || !thinking) return null;

  const lines = thinking.split('\n').filter(line => line.trim() !== '');
  if (lines.length === 0) return null;

  const lastLine = lines[lines.length - 1];
  const currentStatus = lastLine.replace('⚙️', '').trim();

  return (
    <div className="live-status-container blinking">
      <div className="status-indicator">
        <span className="status-icon">⚙️</span>
        <span className="status-text">{currentStatus}...</span>
      </div>
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
      <div className="thinking-title">
        O agente está processando sua pergunta
      </div>

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
  const [threadId, setThreadId] = useState(() => uuidv4());
  const [theme, setTheme] = useState("light");
  const [chatMessages, setChatMessages] = useState([]);
  const [currentThinking, setCurrentThinking] = useState("");

  const bottomRef = useRef(null);
  const textareaRef = useRef(null);
  const currentAssistantIdRef = useRef(null);
  const currentThinkingRef = useRef("");
  const streamMessagesRef = useRef(EMPTY_MESSAGES);
  const thinkingEventsSeenRef = useRef(new Set());
  const previousStreamAssistantIdRef = useRef(null);
  const previousStreamAssistantContentRef = useRef("");

  const toggleTheme = () => setTheme((prev) => (prev === "dark" ? "light" : "dark"));

  const transport = useMemo(() => new FetchStreamTransport({
    apiUrl: `${DEFAULT_API_URL}/chat/stream`,
  }), []);

  const handleCustomEvent = useCallback((event) => {
    if (event?.type === "status" && event?.message) {
      const key = `status:${event.node ?? ""}:${event.message}`;
      if (thinkingEventsSeenRef.current.has(key)) return;
      thinkingEventsSeenRef.current.add(key);

      setCurrentThinking((prev) => {
        const prefix = prev && !prev.endsWith("\n") ? "\n" : "";
        const nextThinking = `${prev}${prefix}⚙️ ${event.message}`;
        currentThinkingRef.current = nextThinking;
        return nextThinking;
      });
    }

    if (event?.type === "done") {
      const assistantId = currentAssistantIdRef.current;
      if (!assistantId) return;

      const lastAssistant = getLastAssistantMessage(streamMessagesRef.current);
      const finalContent = normalizeContent(lastAssistant?.content ?? "");
      const finalThinking = currentThinkingRef.current;

      setChatMessages((prev) => prev.map((msg) =>
        msg.id === assistantId ? { ...msg, content: finalContent || msg.content, thinking: finalThinking || msg.thinking } : msg
      ));

      currentAssistantIdRef.current = null;
      currentThinkingRef.current = "";
      thinkingEventsSeenRef.current.clear();
      setCurrentThinking("");
    }
  }, []);

  const stream = useStream({
    transport,
    threadId,
    messagesKey: "messages",
    initialValues: INITIAL_VALUES,
    onCustomEvent: handleCustomEvent,
    onError: (err) => console.error("Erro no stream:", err),
  });

  const streamMessages = stream.messages ?? EMPTY_MESSAGES;
  const isStreaming = stream.isLoading;
  const error = stream.error;

  useEffect(() => { streamMessagesRef.current = streamMessages; }, [streamMessages]);

  const streamedAssistantContent = useMemo(() => {
    const lastAssistant = getLastAssistantMessage(streamMessages);
    if (!lastAssistant) return "";
    return normalizeContent(lastAssistant.content ?? "");
  }, [streamMessages]);

  const displayMessages = useMemo(() => {
    const activeAssistantId = currentAssistantIdRef.current;
    return chatMessages.map((msg) => ({
      ...msg,
      content: msg.id === activeAssistantId ? streamedAssistantContent || msg.content : msg.content,
    }));
  }, [chatMessages, streamedAssistantContent]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [displayMessages.length, streamedAssistantContent, currentThinking]);

  useEffect(() => {
    if (!textareaRef.current) return;
    textareaRef.current.style.height = "0px";
    textareaRef.current.style.height = `${Math.min(textareaRef.current.scrollHeight, 180)}px`;
  }, [input]);

  const handleSubmit = useCallback((event) => {
    event.preventDefault();
    if (!input.trim() || isStreaming) return;

    const text = input.trim();
    const assistantMessage = { id: `assistant-${threadId}-${Date.now()}`, role: "assistant", content: "", thinking: "" };
    
    currentAssistantIdRef.current = assistantMessage.id;
    setCurrentThinking("");
    setChatMessages((prev) => [...prev, { id: uuidv4(), role: "user", content: text }, assistantMessage]);

    stream.submit({ messages: [{ type: "human", content: text }] }, {
      config: { configurable: { thread_id: threadId, user_id: "web-user" } }
    });
    setInput("");
  }, [input, isStreaming, stream, threadId]);

  const stopStream = useCallback(() => {
    stream.stop();
    currentAssistantIdRef.current = null;
    setCurrentThinking("");
  }, [stream]);

  const clearChat = useCallback(() => {
    stream.stop();
    const newThreadId = uuidv4();
    setThreadId(newThreadId);
    setChatMessages([]);
    setCurrentThinking("");
    currentAssistantIdRef.current = null;
    if (typeof stream.switchThread === "function") stream.switchThread(newThreadId);
  }, [stream]);

  return (
    <div className="app-bg" data-theme={theme}>
      <div className="chat-shell">
        <header className="chat-header">
          <div className="brand">
            <span className="brand-dot" />
            <div>
              <h1>Bússola da Sustentabilidade</h1>
              <p>Assistente de análise de dados</p>
            </div>
          </div>
          <div className="header-actions">
            <button type="button" className="theme-btn" onClick={toggleTheme} aria-label="Alternar tema">
              {theme === "dark" ? <FiSun size={25} /> : <FiMoon size={25} />}
            </button>
            <button type="button" onClick={clearChat} className="ghost-btn">
              <CiCirclePlus size={30} />
            </button>
          </div>
        </header>

        <main className="chat-main">
          {displayMessages.length === 0 ? (
            <section className="empty-state">
              <h2>Faça sua primeira pergunta</h2>
              <p>Converse com o agente em linguagem natural e receba respostas em tempo real.</p>
              <div className="prompt-list">
                {[
                  "Quais cidades têm melhor indicador geral de sustentabilidade?",
                  "Compare Bombinhas e Urubici em turismo e renda.",
                  "Mostre os principais insights de 2023 para SC.",
                  "Quais cidades têm selo de certificação Green Destinations?",

                ].map((p) => (
                  <button key={p} type="button" onClick={() => setInput(p)}>{p}</button>
                ))}
              </div>
            </section>
          ) : (
            displayMessages.map((msg, index) => {
              const isAssistantStreaming = isStreaming && msg.role === "assistant" && msg.id === currentAssistantIdRef.current;
              return (
                <div key={msg.id ?? index} className="message-wrapper">
                  {isAssistantStreaming && !msg.content && (
                    <LiveProcessing thinking={currentThinking} isStreaming={isStreaming} />
                  )}
                  <Message role={msg.role} content={msg.content} />
                </div>
              );
            })
          )}
          <ThinkingTimeline isVisible={isStreaming && !streamedAssistantContent} />
          {error && <div className="error-banner">⚠ {String(error?.message ?? error)}</div>}
          <div ref={bottomRef} />
        </main>

        <form className="chat-input" onSubmit={handleSubmit}>
          <textarea
            ref={textareaRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Digite sua pergunta..."
            rows={1}
            onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); handleSubmit(e); } }}
          />
          <div className="input-actions">
            <span className="hint">Enter envia · Shift + Enter quebra linha</span>
            {isStreaming ? (
              <button type="button" className="stop-btn" onClick={stopStream}>Parar</button>
            ) : (
              <button type="submit" disabled={!input.trim() || isStreaming} className="send-btn">Enviar</button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
}