import React, { useCallback, useEffect, useMemo, useRef, useState } from "react";
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

// --- FUNÇÕES AUXILIARES ---
function normalizeContent(content) {
  if (typeof content === "string") return content;

  if (Array.isArray(content)) {
    return content
      .map((item) => (typeof item === "string" ? item : item?.text || ""))
      .join("\n");
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

function getCurrentStatus(thinking) {
  const lines = thinking?.split("\n").filter((line) => line.trim() !== "") ?? [];

  if (lines.length === 0) {
    return {
      lines,
      currentStatus: "Preparando a análise da sua pergunta",
    };
  }

  const lastLine = lines[lines.length - 1];

  return {
    lines,
    currentStatus: lastLine.replace("⚙️", "").trim(),
  };
}

function formatProcessingTime(ms) {
  const totalSeconds = Math.max(0, Math.floor((ms ?? 0) / 1000));

  return `(${totalSeconds}s)`;
}

// --- COMPONENTES ---
const Message = React.memo(({ role, content, processingMs }) => {
  const isUser = role === "user";
  const processedContent = useMemo(() => normalizeContent(content), [content]);

  const shouldShowProcessingTime =
    !isUser && typeof processingMs === "number" && processingMs >= 0;

  return (
    <div className={`message-row ${isUser ? "is-user" : "is-assistant"}`}>
      {!isUser && (
        <div className="message-avatar assistant-avatar" aria-hidden="true">
          🧭
        </div>
      )}

      <div className={`message-content ${isUser ? "is-user" : "is-assistant"}`}>
        <span className="message-sender">{isUser ? "Você" : "Bússola"}</span>

        <article
          className={[
            "message-bubble",
            isUser ? "is-user" : "is-assistant",
            shouldShowProcessingTime ? "has-processing-time" : "",
          ].join(" ")}
        >
          {processedContent ? (
            <ReactMarkdown remarkPlugins={[remarkGfm]}>{processedContent}</ReactMarkdown>
          ) : (
            !isUser && (
              <div className="typing-container">
                <div className="loading-spinner" aria-hidden="true" />
                <span className="loading-text">Gerando resposta...</span>
              </div>
            )
          )}

          {shouldShowProcessingTime && (
            <span className="bubble-processing-time">
              {formatProcessingTime(processingMs)}
            </span>
          )}
        </article>
      </div>
    </div>
  );
});

function ProcessingBubble({ isVisible, thinking, elapsedMs }) {
  const [activeStep, setActiveStep] = useState(0);

  const { lines, currentStatus } = useMemo(() => getCurrentStatus(thinking), [thinking]);

  const elapsedTime = formatProcessingTime(elapsedMs);

  useEffect(() => {
    if (!isVisible) {
      setActiveStep(0);
      return;
    }

    const eventBasedStep = Math.min(Math.max(lines.length - 1, 0), THINKING_STEPS.length - 1);

    setActiveStep((prev) => Math.max(prev, eventBasedStep));
  }, [isVisible, lines.length]);

  useEffect(() => {
    if (!isVisible) {
      setActiveStep(0);
      return;
    }

    const interval = setInterval(() => {
      setActiveStep((prev) => Math.min(prev + 1, THINKING_STEPS.length - 1));
    }, 1200);

    return () => clearInterval(interval);
  }, [isVisible]);

  if (!isVisible) return null;

  return (
    <div className="processing-row" aria-live="polite">
      <div className="message-avatar assistant-avatar" aria-hidden="true">
        🧭
      </div>

      <div className="processing-content">
        <span className="message-sender">Bússola</span>

        <section className="processing-bubble">
          <div className="processing-header">
            {/* <div className="processing-loader" aria-hidden="true" /> */}

            <div className="processing-header-copy">
              <strong>
                Pensando
                <span className="typing-dots" aria-hidden="true">
                  <span />
                  <span />
                  <span />
                </span>
              </strong>

              <p>{currentStatus}</p>
            </div>
          </div>

          <div className="processing-steps">
            {THINKING_STEPS.map((step, index) => {
              const isDone = index < activeStep;
              const isActive = index === activeStep;

              return (
                <div
                  key={step}
                  className={[
                    "processing-step",
                    isDone ? "is-done" : "",
                    isActive ? "is-active" : "",
                  ].join(" ")}
                >
                  <span className="processing-step-dot" aria-hidden="true" />
                  <span>{step}</span>
                </div>
              );
            })}
          </div>

          <span className="bubble-processing-time">{elapsedTime}</span>
        </section>
      </div>
    </div>
  );
}

// --- APP PRINCIPAL ---
export default function App() {
  const [input, setInput] = useState("");
  const [threadId, setThreadId] = useState(() => uuidv4());
  const [theme, setTheme] = useState("light");
  const [chatMessages, setChatMessages] = useState([]);
  const [currentThinking, setCurrentThinking] = useState("");
  const [elapsedMs, setElapsedMs] = useState(0);

  const bottomRef = useRef(null);
  const textareaRef = useRef(null);
  const currentAssistantIdRef = useRef(null);
  const currentThinkingRef = useRef("");
  const streamMessagesRef = useRef(EMPTY_MESSAGES);
  const thinkingEventsSeenRef = useRef(new Set());
  const processingStartedAtRef = useRef(null);

  const toggleTheme = () => setTheme((prev) => (prev === "dark" ? "light" : "dark"));

  const transport = useMemo(
    () =>
      new FetchStreamTransport({
        apiUrl: `${DEFAULT_API_URL}/chat/stream`,
      }),
    []
  );

  const handleCustomEvent = useCallback((event) => {
    if (event?.type === "status" && event?.message) {
      const key = `status:${event.node ?? ""}:${event.message}`;

      if (thinkingEventsSeenRef.current.has(key)) return;

      thinkingEventsSeenRef.current.add(key);

      setCurrentThinking((prev) => {
        const next = `${prev}${prev ? "\n" : ""}⚙️ ${event.message}`;
        currentThinkingRef.current = next;
        return next;
      });
    }

    if (event?.type === "done") {
      const assistantId = currentAssistantIdRef.current;

      if (!assistantId) return;

      const finalProcessingMs = processingStartedAtRef.current
        ? Date.now() - processingStartedAtRef.current
        : elapsedMs;

      const lastAssistant = getLastAssistantMessage(streamMessagesRef.current);
      const finalContent = normalizeContent(lastAssistant?.content ?? "");

      setChatMessages((prev) =>
        prev.map((msg) =>
          msg.id === assistantId
            ? {
                ...msg,
                content: finalContent || msg.content,
                thinking: currentThinkingRef.current,
                processingMs: finalProcessingMs,
              }
            : msg
        )
      );

      currentAssistantIdRef.current = null;
      currentThinkingRef.current = "";
      thinkingEventsSeenRef.current.clear();
      processingStartedAtRef.current = null;
      setCurrentThinking("");
      setElapsedMs(0);
    }
  }, [elapsedMs]);

  const stream = useStream({
    transport,
    threadId,
    messagesKey: "messages",
    initialValues: INITIAL_VALUES,
    onCustomEvent: handleCustomEvent,
    onError: (err) => console.error("Erro no stream:", err),
  });

  const isStreaming = stream.isLoading;
  const streamError = stream.error;

  useEffect(() => {
  if (!isStreaming || !processingStartedAtRef.current) return;

  const updateElapsedTime = () => {
    setElapsedMs(Date.now() - processingStartedAtRef.current);
  };

  updateElapsedTime();

  const interval = setInterval(updateElapsedTime, 250);

  return () => clearInterval(interval);
}, [isStreaming]);

  useEffect(() => {
    streamMessagesRef.current = stream.messages ?? EMPTY_MESSAGES;
  }, [stream.messages]);

  const streamedAssistantContent = useMemo(() => {
    const lastAssistant = getLastAssistantMessage(stream.messages ?? []);

    if (!lastAssistant) return "";

    return normalizeContent(lastAssistant.content ?? "");
  }, [stream.messages]);

  const displayMessages = useMemo(() => {
    const activeId = currentAssistantIdRef.current;

    return chatMessages.map((msg) => {
      if (msg.id === activeId) {
        return {
          ...msg,
          content: streamedAssistantContent || msg.content,
          processingMs: isStreaming ? elapsedMs : msg.processingMs,
        };
      }

      return msg;
    });
  }, [chatMessages, streamedAssistantContent, isStreaming, elapsedMs]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "auto" });
  }, [displayMessages.length, isStreaming, currentThinking, streamedAssistantContent, elapsedMs]);

  useEffect(() => {
    if (!textareaRef.current) return;

    textareaRef.current.style.height = "0px";
    textareaRef.current.style.height = `${Math.min(textareaRef.current.scrollHeight, 180)}px`;
  }, [input]);

  const handleSubmit = useCallback(
    (event) => {
      event.preventDefault();

      if (!input.trim() || isStreaming) return;

      const text = input.trim();
      const assistantId = `assistant-${Date.now()}`;

      processingStartedAtRef.current = Date.now();
      setElapsedMs(0);

      currentAssistantIdRef.current = assistantId;
      currentThinkingRef.current = "";
      thinkingEventsSeenRef.current.clear();
      setCurrentThinking("");

      setChatMessages((prev) => [
        ...prev,
        {
          id: uuidv4(),
          role: "user",
          content: text,
        },
        {
          id: assistantId,
          role: "assistant",
          content: "",
          thinking: "",
          processingMs: 0,
        },
      ]);

      stream.submit(
        {
          messages: [
            {
              type: "human",
              content: text,
            },
          ],
        },
        {
          config: {
            configurable: {
              thread_id: threadId,
              user_id: "web-user",
            },
          },
        }
      );

      setInput("");
    },
    [input, isStreaming, stream, threadId]
  );

  const clearChat = useCallback(() => {
    stream.stop();

    const newThreadId = uuidv4();

    setThreadId(newThreadId);
    setChatMessages([]);
    setCurrentThinking("");

    currentAssistantIdRef.current = null;
    currentThinkingRef.current = "";
    thinkingEventsSeenRef.current.clear();
    processingStartedAtRef.current = null;
    setElapsedMs(0);

    if (typeof stream.switchThread === "function") {
      stream.switchThread(newThreadId);
    }
  }, [stream]);

  return (
    <div className="app-bg" data-theme={theme}>
      <div className="chat-shell">
        <header className="chat-header">
          <div className="brand">
            <span className="brand-dot" aria-hidden="true" />

            <div>
              <h1>Bússola da Sustentabilidade</h1>
              <p>Assistente de análise de dados</p>
            </div>
          </div>

          <div className="header-actions">
            <button
              type="button"
              className="theme-btn"
              onClick={toggleTheme}
              aria-label={theme === "dark" ? "Ativar tema claro" : "Ativar tema escuro"}
              title={theme === "dark" ? "Ativar tema claro" : "Ativar tema escuro"}
            >
              {theme === "dark" ? <FiSun size={22} /> : <FiMoon size={22} />}
            </button>

            <button
              type="button"
              onClick={clearChat}
              className="ghost-btn"
              aria-label="Iniciar nova conversa"
              title="Iniciar nova conversa"
            >
              <CiCirclePlus size={26} />
            </button>
          </div>
        </header>

        <main className="chat-main">
          {displayMessages.length === 0 ? (
            <section className="empty-state">
              <div className="icon-buss-container">
                <div className="icon-buss" aria-hidden="true">
                  🧭
                </div>
              </div>

              <h2>Faça sua primeira pergunta</h2>

              <p>
                Converse com o agente em linguagem natural e receba respostas em tempo
                real sobre os indicadores de sustentabilidade.
              </p>

              <div className="prompt-list">
                {[
                  "Quais cidades têm melhor indicador geral de sustentabilidade?",
                  "Compare Bombinhas e Urubici em turismo e renda.",
                  "Mostre os principais insights de 2023 para SC.",
                  "Quais cidades têm selo de certificação Green Destinations?",
                ].map((p) => (
                  <button key={p} type="button" onClick={() => setInput(p)}>
                    {p}
                  </button>
                ))}
              </div>
            </section>
          ) : (
            displayMessages.map((msg, index) => {
              const isAssistantStreaming =
                isStreaming &&
                msg.role === "assistant" &&
                msg.id === currentAssistantIdRef.current;

              return (
                <div key={msg.id ?? index} className="message-wrapper">
                  {isAssistantStreaming && !msg.content ? (
                    <ProcessingBubble
                      isVisible={isAssistantStreaming}
                      thinking={currentThinking}
                      elapsedMs={elapsedMs}
                    />
                  ) : (
                    <Message
                      role={msg.role}
                      content={msg.content}
                      processingMs={msg.processingMs}
                    />
                  )}
                </div>
              );
            })
          )}

          {streamError && (
            <div className="error-banner">
              ⚠ {String(streamError.message || streamError)}
            </div>
          )}

          <div ref={bottomRef} />
        </main>

        <form className="chat-input" onSubmit={handleSubmit}>
          <textarea
            ref={textareaRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Digite sua pergunta..."
            rows={1}
            aria-label="Digite sua pergunta"
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                handleSubmit(e);
              }
            }}
          />

          <div className="input-actions">
            <span className="hint">Enter envia · Shift + Enter quebra linha</span>

            <button
              type="submit"
              disabled={!input.trim() || isStreaming}
              className="send-btn"
            >
              {isStreaming ? "Processando..." : "Enviar"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}