/**
 * BussolaChat.jsx
 *
 * Interface de chat para o Projeto Bússola da Sustentabilidade.
 * Conecta ao endpoint /chat/stream via FetchStreamTransport do @langchain/react,
 * consumindo Server-Sent Events em tempo real.
 *
 * Dependências (instalar no projeto React):
 *   npm install @langchain/react uuid
 *
 * O componente pode ser usado standalone:
 *   import BussolaChat from "./BussolaChat";
 *   <BussolaChat apiUrl="http://localhost:8000" userId="usuario-01" />
 */

import { useState, useEffect, useRef, useCallback } from "react";
import { v4 as uuidv4 } from "uuid";

// ─── Constante de URL padrão ──────────────────────────────────────────────────
const DEFAULT_API_URL = "http://localhost:8000";

// ─── Hook de streaming customizado ───────────────────────────────────────────
/**
 * useStreamChat
 *
 * Abstrai o FetchStreamTransport / SSE de forma simples para este projeto.
 * Se o pacote @langchain/react estiver disponível, você pode substituir
 * este hook pelo useStream oficial — veja o comentário abaixo.
 *
 * Para usar o hook oficial do LangChain (requer @langchain/react instalado):
 *
 *   import { useStream, FetchStreamTransport } from "@langchain/react";
 *
 *   const stream = useStream({
 *     transport: new FetchStreamTransport({
 *       apiUrl: `${apiUrl}/chat/stream`,
 *     }),
 *   });
 *
 * Este hook customizado replica o comportamento essencial sem dependência
 * adicional, sendo totalmente compatível com o backend SSE implementado.
 */
function useStreamChat({ apiUrl, threadId, userId }) {
  const [messages, setMessages] = useState([]);
  const [isStreaming, setIsStreaming] = useState(false);
  const [error, setError] = useState(null);
  const abortRef = useRef(null);

  const sendMessage = useCallback(
    async (text) => {
      if (!text.trim() || isStreaming) return;

      // Adiciona a mensagem do usuário imediatamente
      const userMsg = { id: uuidv4(), role: "user", content: text };
      setMessages((prev) => [...prev, userMsg]);
      setIsStreaming(true);
      setError(null);

      // Placeholder da resposta do assistente (será atualizado token a token)
      const assistantId = `msg-${threadId}`;
      setMessages((prev) => [
        ...prev,
        { id: assistantId, role: "assistant", content: "" },
      ]);

      const controller = new AbortController();
      abortRef.current = controller;

      try {
        const response = await fetch(`${apiUrl}/chat/stream`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: text, thread_id: threadId, user_id: userId }),
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = "";

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });

          // Processa cada linha SSE completa
          const lines = buffer.split("\n");
          buffer = lines.pop(); // guarda linha incompleta

          for (const line of lines) {
            const trimmed = line.trim();
            if (!trimmed.startsWith("data:")) continue;

            const jsonStr = trimmed.slice(5).trim();
            if (!jsonStr) continue;

            try {
              const parsed = JSON.parse(jsonStr);
              const { event, data } = parsed;

              if (event === "messages/partial" && Array.isArray(data)) {
                const partial = data[0];
                if (partial?.content) {
                  setMessages((prev) =>
                    prev.map((m) =>
                      m.id === assistantId
                        ? { ...m, content: partial.content }
                        : m
                    )
                  );
                }
              }

              if (event === "messages/complete" && Array.isArray(data)) {
                const complete = data[0];
                if (complete?.content) {
                  setMessages((prev) =>
                    prev.map((m) =>
                      m.id === assistantId
                        ? { ...m, content: complete.content }
                        : m
                    )
                  );
                }
              }

              if (event === "error") {
                setError(data?.message || "Erro desconhecido no servidor.");
              }
            } catch {
              // linha SSE mal-formada — ignorar
            }
          }
        }
      } catch (err) {
        if (err.name !== "AbortError") {
          setError(err.message);
          // Remove o placeholder vazio se houve erro antes de qualquer conteúdo
          setMessages((prev) =>
            prev.filter((m) => !(m.id === assistantId && m.content === ""))
          );
        }
      } finally {
        setIsStreaming(false);
        abortRef.current = null;
      }
    },
    [apiUrl, threadId, userId, isStreaming]
  );

  const stopStream = useCallback(() => {
    abortRef.current?.abort();
  }, []);

  const clearMessages = useCallback(() => {
    setMessages([]);
    setError(null);
  }, []);

  return { messages, isStreaming, error, sendMessage, stopStream, clearMessages };
}

// ─── Componente principal ─────────────────────────────────────────────────────
export default function BussolaChat({
  apiUrl = DEFAULT_API_URL,
  userId = "usuario-anonimo",
}) {
  const [input, setInput] = useState("");
  // threadId fixo por sessão do componente
  const [threadId] = useState(() => uuidv4());
  const bottomRef = useRef(null);
  const textareaRef = useRef(null);

  const { messages, isStreaming, error, sendMessage, stopStream, clearMessages } =
    useStreamChat({ apiUrl, threadId, userId });

  // Rola para a última mensagem automaticamente
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSubmit = (e) => {
    e?.preventDefault();
    if (!input.trim() || isStreaming) return;
    sendMessage(input.trim());
    setInput("");
    textareaRef.current?.focus();
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div style={styles.root}>
      {/* ── Cabeçalho ── */}
      <header style={styles.header}>
        <div style={styles.headerInner}>
          <div style={styles.logoMark}>
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
              <circle cx="12" cy="12" r="10" stroke="#4ade80" strokeWidth="1.5" />
              <path d="M12 2 L12 12 L17 7" stroke="#4ade80" strokeWidth="1.5" strokeLinecap="round" />
            </svg>
          </div>
          <div>
            <h1 style={styles.title}>Bússola da Sustentabilidade</h1>
            <p style={styles.subtitle}>Análise inteligente de dados turísticos</p>
          </div>
        </div>
        <button onClick={clearMessages} style={styles.clearBtn} title="Nova conversa">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8" />
            <path d="M3 3v5h5" />
          </svg>
        </button>
      </header>

      {/* ── Área de mensagens ── */}
      <main style={styles.messages}>
        {messages.length === 0 && (
          <div style={styles.empty}>
            <div style={styles.emptyIcon}>
              <svg width="40" height="40" viewBox="0 0 24 24" fill="none">
                <circle cx="12" cy="12" r="10" stroke="#334155" strokeWidth="1" />
                <path d="M12 2 L12 12 L17 7" stroke="#334155" strokeWidth="1.5" strokeLinecap="round" />
              </svg>
            </div>
            <p style={styles.emptyTitle}>Como posso ajudar?</p>
            <p style={styles.emptyHint}>
              Pergunte sobre cidades, ranking de sustentabilidade, indicadores
              turísticos ou qualquer dado disponível na base Bússola.
            </p>
            <div style={styles.suggestions}>
              {[
                "Quais são as 5 cidades com maior aproveitamento Green Destinations?",
                "Compare os indicadores de sustentabilidade de Bombinhas e Urubici.",
                "Qual a média salarial do setor de turismo em SC?",
              ].map((s) => (
                <button
                  key={s}
                  style={styles.suggestion}
                  onClick={() => { setInput(s); textareaRef.current?.focus(); }}
                >
                  {s}
                </button>
              ))}
            </div>
          </div>
        )}

        {messages.map((msg) => (
          <MessageBubble key={msg.id} message={msg} />
        ))}

        {/* Indicador de digitação enquanto não há tokens ainda */}
        {isStreaming && messages[messages.length - 1]?.role === "assistant" &&
          messages[messages.length - 1]?.content === "" && (
            <div style={{ ...styles.bubble, ...styles.bubbleAssistant }}>
              <TypingIndicator />
            </div>
          )}

        {error && (
          <div style={styles.errorBanner}>
            <span>⚠ {error}</span>
            <button onClick={() => {}} style={styles.errorDismiss}>×</button>
          </div>
        )}

        <div ref={bottomRef} />
      </main>

      {/* ── Input ── */}
      <form onSubmit={handleSubmit} style={styles.inputArea}>
        <div style={styles.inputWrapper}>
          <textarea
            ref={textareaRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Faça uma pergunta sobre os dados de sustentabilidade…"
            rows={1}
            style={styles.textarea}
            disabled={isStreaming}
          />
          {isStreaming ? (
            <button type="button" onClick={stopStream} style={styles.stopBtn}>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <rect x="6" y="6" width="12" height="12" rx="2" />
              </svg>
            </button>
          ) : (
            <button
              type="submit"
              disabled={!input.trim()}
              style={{
                ...styles.sendBtn,
                ...(!input.trim() ? styles.sendBtnDisabled : {}),
              }}
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M22 2L11 13" />
                <path d="M22 2L15 22 11 13 2 9l20-7z" />
              </svg>
            </button>
          )}
        </div>
        <p style={styles.footer}>
          thread: <code style={styles.code}>{threadId.slice(0, 8)}…</code>
          &nbsp;·&nbsp;
          <kbd style={styles.kbd}>Enter</kbd> para enviar &nbsp;
          <kbd style={styles.kbd}>Shift+Enter</kbd> para quebrar linha
        </p>
      </form>
    </div>
  );
}

// ─── Sub-componentes ──────────────────────────────────────────────────────────

function MessageBubble({ message }) {
  const isUser = message.role === "user";
  return (
    <div style={{ ...styles.messageRow, ...(isUser ? styles.messageRowUser : {}) }}>
      {!isUser && (
        <div style={styles.avatar}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="10" stroke="#4ade80" strokeWidth="2" />
            <path d="M12 2 L12 12 L17 7" stroke="#4ade80" strokeWidth="2" strokeLinecap="round" />
          </svg>
        </div>
      )}
      <div
        style={{
          ...styles.bubble,
          ...(isUser ? styles.bubbleUser : styles.bubbleAssistant),
        }}
      >
        <FormattedContent content={message.content} />
      </div>
    </div>
  );
}

/**
 * FormattedContent
 * Renderiza texto com suporte básico a markdown:
 * negrito (**texto**), código inline (`code`), blocos de código (```...```)
 * e quebras de linha.
 */
function FormattedContent({ content }) {
  if (!content) return null;

  // Separa blocos de código do restante
  const parts = content.split(/(```[\s\S]*?```)/g);

  return (
    <div style={styles.contentWrapper}>
      {parts.map((part, i) => {
        if (part.startsWith("```")) {
          const code = part.replace(/^```[^\n]*\n?/, "").replace(/```$/, "");
          return (
            <pre key={i} style={styles.codeBlock}>
              <code>{code}</code>
            </pre>
          );
        }

        // Inline: negrito e code
        return (
          <span key={i}>
            {part.split("\n").map((line, j) => (
              <span key={j}>
                {j > 0 && <br />}
                {renderInline(line)}
              </span>
            ))}
          </span>
        );
      })}
    </div>
  );
}

function renderInline(text) {
  const tokens = text.split(/(\*\*[^*]+\*\*|`[^`]+`)/g);
  return tokens.map((token, i) => {
    if (token.startsWith("**") && token.endsWith("**")) {
      return <strong key={i}>{token.slice(2, -2)}</strong>;
    }
    if (token.startsWith("`") && token.endsWith("`")) {
      return <code key={i} style={styles.inlineCode}>{token.slice(1, -1)}</code>;
    }
    return token;
  });
}

function TypingIndicator() {
  return (
    <div style={styles.typing}>
      {[0, 1, 2].map((i) => (
        <span
          key={i}
          style={{
            ...styles.dot,
            animationDelay: `${i * 0.18}s`,
          }}
        />
      ))}
    </div>
  );
}

// ─── Estilos ──────────────────────────────────────────────────────────────────
const palette = {
  bg: "#0a0f1a",
  surface: "#111827",
  surfaceHover: "#1e293b",
  border: "#1e293b",
  borderLight: "#273344",
  text: "#e2e8f0",
  textMuted: "#64748b",
  textFaint: "#334155",
  accent: "#4ade80",
  accentDim: "#166534",
  user: "#1d4ed8",
  userBg: "#1e3a8a",
  error: "#ef4444",
  errorBg: "#1c0a0a",
};

const styles = {
  root: {
    display: "flex",
    flexDirection: "column",
    height: "100vh",
    background: palette.bg,
    fontFamily: "'IBM Plex Mono', 'Fira Code', 'Courier New', monospace",
    color: palette.text,
    overflow: "hidden",
  },

  // Header
  header: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    padding: "14px 20px",
    borderBottom: `1px solid ${palette.border}`,
    background: palette.surface,
    flexShrink: 0,
  },
  headerInner: {
    display: "flex",
    alignItems: "center",
    gap: 12,
  },
  logoMark: {
    width: 36,
    height: 36,
    borderRadius: 8,
    background: "#0d1a12",
    border: `1px solid ${palette.accentDim}`,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  title: {
    margin: 0,
    fontSize: 15,
    fontWeight: 600,
    letterSpacing: "0.02em",
    color: palette.text,
  },
  subtitle: {
    margin: 0,
    fontSize: 11,
    color: palette.textMuted,
    letterSpacing: "0.04em",
    textTransform: "uppercase",
  },
  clearBtn: {
    background: "none",
    border: `1px solid ${palette.border}`,
    borderRadius: 6,
    color: palette.textMuted,
    cursor: "pointer",
    padding: "6px 8px",
    display: "flex",
    alignItems: "center",
    transition: "color 0.15s, border-color 0.15s",
  },

  // Messages
  messages: {
    flex: 1,
    overflowY: "auto",
    padding: "24px 20px",
    display: "flex",
    flexDirection: "column",
    gap: 16,
  },

  // Empty state
  empty: {
    margin: "auto",
    textAlign: "center",
    maxWidth: 480,
    padding: "40px 0",
  },
  emptyIcon: {
    marginBottom: 20,
    opacity: 0.4,
  },
  emptyTitle: {
    fontSize: 18,
    fontWeight: 600,
    color: palette.text,
    margin: "0 0 8px",
  },
  emptyHint: {
    fontSize: 13,
    color: palette.textMuted,
    lineHeight: 1.6,
    margin: "0 0 24px",
  },
  suggestions: {
    display: "flex",
    flexDirection: "column",
    gap: 8,
    alignItems: "stretch",
  },
  suggestion: {
    background: palette.surface,
    border: `1px solid ${palette.border}`,
    borderRadius: 8,
    color: palette.text,
    cursor: "pointer",
    fontSize: 12,
    padding: "10px 14px",
    textAlign: "left",
    transition: "border-color 0.15s, background 0.15s",
    fontFamily: "inherit",
    lineHeight: 1.5,
  },

  // Message rows
  messageRow: {
    display: "flex",
    gap: 10,
    alignItems: "flex-start",
    maxWidth: 760,
    width: "100%",
  },
  messageRowUser: {
    alignSelf: "flex-end",
    flexDirection: "row-reverse",
  },
  avatar: {
    width: 28,
    height: 28,
    borderRadius: 6,
    background: "#0d1a12",
    border: `1px solid ${palette.accentDim}`,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    flexShrink: 0,
    marginTop: 2,
  },

  // Bubbles
  bubble: {
    borderRadius: 10,
    padding: "10px 14px",
    fontSize: 13.5,
    lineHeight: 1.65,
    maxWidth: "calc(100% - 40px)",
    wordBreak: "break-word",
  },
  bubbleUser: {
    background: palette.userBg,
    border: `1px solid ${palette.user}`,
    color: "#bfdbfe",
  },
  bubbleAssistant: {
    background: palette.surface,
    border: `1px solid ${palette.border}`,
    color: palette.text,
  },

  // Formatted content
  contentWrapper: {
    whiteSpace: "pre-wrap",
  },
  codeBlock: {
    background: "#0d1117",
    border: `1px solid ${palette.border}`,
    borderRadius: 6,
    padding: "10px 12px",
    fontSize: 12,
    overflowX: "auto",
    margin: "8px 0",
    fontFamily: "inherit",
    color: "#86efac",
  },
  inlineCode: {
    background: "#1e293b",
    borderRadius: 3,
    padding: "1px 5px",
    fontSize: "0.9em",
    color: "#86efac",
    fontFamily: "inherit",
  },

  // Typing indicator
  typing: {
    display: "flex",
    gap: 5,
    alignItems: "center",
    padding: "4px 2px",
  },
  dot: {
    width: 6,
    height: 6,
    borderRadius: "50%",
    background: palette.textMuted,
    animation: "blink 1.2s infinite ease-in-out",
    display: "inline-block",
  },

  // Error banner
  errorBanner: {
    background: palette.errorBg,
    border: `1px solid ${palette.error}`,
    borderRadius: 8,
    color: palette.error,
    fontSize: 12,
    padding: "10px 14px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },
  errorDismiss: {
    background: "none",
    border: "none",
    color: palette.error,
    cursor: "pointer",
    fontSize: 18,
    padding: 0,
    lineHeight: 1,
  },

  // Input area
  inputArea: {
    borderTop: `1px solid ${palette.border}`,
    padding: "16px 20px 12px",
    background: palette.surface,
    flexShrink: 0,
  },
  inputWrapper: {
    display: "flex",
    gap: 8,
    alignItems: "flex-end",
  },
  textarea: {
    flex: 1,
    background: palette.bg,
    border: `1px solid ${palette.borderLight}`,
    borderRadius: 8,
    color: palette.text,
    fontFamily: "inherit",
    fontSize: 13.5,
    lineHeight: 1.6,
    outline: "none",
    padding: "10px 14px",
    resize: "none",
    maxHeight: 160,
    overflowY: "auto",
    transition: "border-color 0.15s",
  },
  sendBtn: {
    background: palette.accent,
    border: "none",
    borderRadius: 8,
    color: "#052e16",
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    height: 40,
    width: 40,
    flexShrink: 0,
    transition: "opacity 0.15s",
  },
  sendBtnDisabled: {
    opacity: 0.35,
    cursor: "not-allowed",
  },
  stopBtn: {
    background: palette.errorBg,
    border: `1px solid ${palette.error}`,
    borderRadius: 8,
    color: palette.error,
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    height: 40,
    width: 40,
    flexShrink: 0,
  },
  footer: {
    color: palette.textFaint,
    fontSize: 11,
    margin: "8px 0 0",
    letterSpacing: "0.02em",
  },
  code: {
    fontFamily: "inherit",
    color: palette.textMuted,
  },
  kbd: {
    background: palette.surfaceHover,
    border: `1px solid ${palette.border}`,
    borderRadius: 3,
    color: palette.textMuted,
    fontSize: 10,
    padding: "1px 5px",
    fontFamily: "inherit",
  },
};

// Injeta animação CSS para os pontos de digitação
if (typeof document !== "undefined") {
  const style = document.createElement("style");
  style.textContent = `
    @keyframes blink {
      0%, 80%, 100% { opacity: 0.2; transform: scale(0.9); }
      40% { opacity: 1; transform: scale(1.1); }
    }
    textarea:focus {
      border-color: #166534 !important;
    }
    button:hover:not(:disabled) {
      opacity: 0.85;
    }
  `;
  document.head.appendChild(style);
}