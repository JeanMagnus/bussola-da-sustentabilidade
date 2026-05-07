import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { v4 as uuidv4 } from "uuid";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { CiCirclePlus } from "react-icons/ci";
import { FiDownload, FiFileText, FiMoon, FiSend, FiSun } from "react-icons/fi";
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
        <span className="message-sender">{isUser ? "Você" : "Bússola"}</span>

        <article className={`message-bubble ${isUser ? "is-user" : "is-assistant"}`}>
          {content ? (
            <ReactMarkdown remarkPlugins={[remarkGfm]}>{normalizeContent(content)}</ReactMarkdown>
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

  const lines = thinking.split("\n").filter((line) => line.trim() !== "");
  if (lines.length === 0) return null;

  const lastLine = lines[lines.length - 1];
  const currentStatus = lastLine.replace("⚙️", "").trim();

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
    if (!isVisible) return undefined;

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

function statusTone(status) {
  if (status === "approved") return "approved";
  if (status === "rejected") return "rejected";
  return "pending";
}

function ReportWorkspace() {
  const [templates, setTemplates] = useState([]);
  const [reports, setReports] = useState([]);
  const [selectedTemplate, setSelectedTemplate] = useState("");
  const [requestedBy, setRequestedBy] = useState("Usuário solicitante");
  const [validator, setValidator] = useState("Validador responsável");
  const [instructions, setInstructions] = useState("");
  const [activeReport, setActiveReport] = useState(null);
  const [validationNotes, setValidationNotes] = useState("");
  const [isGenerating, setIsGenerating] = useState(false);
  const [notice, setNotice] = useState("");

  const loadReports = useCallback(async () => {
    const response = await fetch(`${DEFAULT_API_URL}/reports`);
    const data = await response.json();
    setReports(data.reports ?? []);
  }, []);

  useEffect(() => {
    async function loadInitialData() {
      const templateResponse = await fetch(`${DEFAULT_API_URL}/reports/templates`);
      const templateData = await templateResponse.json();
      setTemplates(templateData.templates ?? []);
      setSelectedTemplate((templateData.templates ?? [])[0]?.id ?? "");
      await loadReports();
    }

    loadInitialData();
  }, [loadReports]);

  const handleGenerateReport = async (event) => {
    event.preventDefault();
    if (!selectedTemplate || !instructions.trim()) return;

    setIsGenerating(true);
    setNotice("O agente está escrevendo no template PDF selecionado...");

    const response = await fetch(`${DEFAULT_API_URL}/reports`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        template_id: selectedTemplate,
        requested_by: requestedBy,
        validator,
        instructions,
      }),
    });

    const data = await response.json();
    setActiveReport(data);
    setValidationNotes("");
    setInstructions("");
    setIsGenerating(false);
    setNotice("Prévia criada e enviada para validação. O download ficará bloqueado até a aprovação.");
    await loadReports();
  };

  const openReport = async (reportId) => {
    const response = await fetch(`${DEFAULT_API_URL}/reports/${reportId}`);
    const data = await response.json();
    setActiveReport(data);
    setValidationNotes(data.validator_notes ?? "");
    setNotice("");
  };

  const handleValidate = async (decision) => {
    if (!activeReport) return;

    const response = await fetch(`${DEFAULT_API_URL}/reports/${activeReport.id}/validation`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ decision, notes: validationNotes }),
    });
    const data = await response.json();
    setActiveReport(data);
    setNotice(decision === "approved" ? "Relatório aprovado. Download liberado ao solicitante." : "Relatório reprovado. Download permanece bloqueado.");
    await loadReports();
  };

  const handleDownload = () => {
    if (!activeReport || activeReport.status !== "approved") return;
    window.open(`${DEFAULT_API_URL}/reports/${activeReport.id}/download`, "_blank", "noopener,noreferrer");
  };

  return (
    <main className="reports-main">
      <section className="report-builder-card">
        <div className="section-eyebrow">Novo relatório</div>
        <h2>Escrever em template PDF</h2>
        <p>
          Escolha um template, descreva as informações desejadas e envie o PDF gerado para validação antes da liberação do download.
        </p>

        <form className="report-form" onSubmit={handleGenerateReport}>
          <label>
            Template PDF
            <div className="template-grid">
              {templates.map((template) => (
                <button
                  key={template.id}
                  type="button"
                  className={`template-option ${selectedTemplate === template.id ? "selected" : ""}`}
                  onClick={() => setSelectedTemplate(template.id)}
                >
                  <FiFileText />
                  <strong>{template.name}</strong>
                  <span>{template.description}</span>
                </button>
              ))}
            </div>
          </label>

          <div className="form-row">
            <label>
              Solicitante
              <input value={requestedBy} onChange={(event) => setRequestedBy(event.target.value)} />
            </label>
            <label>
              Usuário validador
              <input value={validator} onChange={(event) => setValidator(event.target.value)} />
            </label>
          </div>

          <label>
            Informações que o agente deve escrever no relatório
            <textarea
              value={instructions}
              onChange={(event) => setInstructions(event.target.value)}
              placeholder="Ex.: gerar um resumo executivo comparando Bombinhas e Urubici, destacar indicadores positivos, riscos e recomendações para validação."
              rows={6}
            />
          </label>

          <button className="generate-report-btn" type="submit" disabled={isGenerating || !instructions.trim()}>
            <FiSend /> {isGenerating ? "Gerando relatório..." : "Gerar e enviar para validação"}
          </button>
        </form>

        {notice && <div className="report-notice">{notice}</div>}
      </section>

      <section className="report-preview-card">
        <div className="section-eyebrow">Prévia controlada</div>
        <div className="preview-header">
          <div>
            <h2>{activeReport ? activeReport.template.name : "Nenhum relatório selecionado"}</h2>
            <p>{activeReport ? activeReport.status_label : "Gere ou selecione um relatório para visualizar."}</p>
          </div>
          {activeReport && <span className={`status-pill ${statusTone(activeReport.status)}`}>{activeReport.status_label}</span>}
        </div>

        {activeReport ? (
          <>
            <div className="preview-toolbar">
              <span>Download bloqueado na prévia. Somente imagens são exibidas até a aprovação.</span>
              <button type="button" onClick={handleDownload} disabled={activeReport.status !== "approved"}>
                <FiDownload /> Baixar PDF
              </button>
            </div>

            <div className="pdf-preview" onContextMenu={(event) => event.preventDefault()}>
              {(activeReport.preview_pages ?? []).map((page, index) => (
                <div className="preview-page-frame" key={`${activeReport.id}-${index}`}>
                  <span className="preview-watermark">PRÉVIA SEM DOWNLOAD</span>
                  <img src={page} alt={`Página ${index + 1} do relatório`} draggable="false" />
                </div>
              ))}
            </div>

            <div className="validation-panel">
              <h3>Área do usuário validador</h3>
              <p>Validador atribuído: <strong>{activeReport.validator}</strong></p>
              <textarea
                value={validationNotes}
                onChange={(event) => setValidationNotes(event.target.value)}
                placeholder="Observações da validação (opcional)"
                rows={3}
              />
              <div className="validation-actions">
                <button type="button" className="reject-btn" onClick={() => handleValidate("rejected")}>Reprovar</button>
                <button type="button" className="approve-btn" onClick={() => handleValidate("approved")}>Aprovar e liberar download</button>
              </div>
            </div>
          </>
        ) : (
          <div className="empty-preview">A prévia aparecerá aqui como imagem, evitando acesso direto ao PDF antes da validação.</div>
        )}
      </section>

      <aside className="validation-queue-card">
        <div className="section-eyebrow">Fila de validação</div>
        <h2>Relatórios recentes</h2>
        <div className="report-list">
          {reports.length === 0 ? (
            <p>Nenhum relatório gerado ainda.</p>
          ) : (
            reports.map((report) => (
              <button key={report.id} type="button" onClick={() => openReport(report.id)} className={activeReport?.id === report.id ? "active" : ""}>
                <strong>{report.template.name}</strong>
                <span>{report.requested_by} → {report.validator}</span>
                <small className={`status-text-${statusTone(report.status)}`}>{report.status_label}</small>
              </button>
            ))
          )}
        </div>
      </aside>
    </main>
  );
}

export default function App() {
  const [input, setInput] = useState("");
  const [threadId, setThreadId] = useState(() => uuidv4());
  const [theme, setTheme] = useState("light");
  const [chatMessages, setChatMessages] = useState([]);
  const [currentThinking, setCurrentThinking] = useState("");
  const [activeView, setActiveView] = useState("chat");
  const [activeAssistantId, setActiveAssistantId] = useState(null);

  const bottomRef = useRef(null);
  const textareaRef = useRef(null);
  const currentAssistantIdRef = useRef(null);
  const currentThinkingRef = useRef("");
  const streamMessagesRef = useRef(EMPTY_MESSAGES);
  const thinkingEventsSeenRef = useRef(new Set());

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

      setChatMessages((prev) => prev.map((msg) => (
        msg.id === assistantId ? { ...msg, content: finalContent || msg.content, thinking: finalThinking || msg.thinking } : msg
      )));

      currentAssistantIdRef.current = null;
      setActiveAssistantId(null);
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
    return chatMessages.map((msg) => ({
      ...msg,
      content: msg.id === activeAssistantId ? streamedAssistantContent || msg.content : msg.content,
    }));
  }, [activeAssistantId, chatMessages, streamedAssistantContent]);

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
    setActiveAssistantId(assistantMessage.id);
    setCurrentThinking("");
    setChatMessages((prev) => [...prev, { id: uuidv4(), role: "user", content: text }, assistantMessage]);

    stream.submit({ messages: [{ type: "human", content: text }] }, {
      config: { configurable: { thread_id: threadId, user_id: "web-user" } },
    });
    setInput("");
  }, [input, isStreaming, stream, threadId]);

  const stopStream = useCallback(() => {
    stream.stop();
    currentAssistantIdRef.current = null;
    setActiveAssistantId(null);
    setCurrentThinking("");
  }, [stream]);

  const clearChat = useCallback(() => {
    stream.stop();
    const newThreadId = uuidv4();
    setThreadId(newThreadId);
    setChatMessages([]);
    setCurrentThinking("");
    currentAssistantIdRef.current = null;
    setActiveAssistantId(null);
    if (typeof stream.switchThread === "function") stream.switchThread(newThreadId);
  }, [stream]);

  return (
    <div className="app-bg" data-theme={theme}>
      <div className={`chat-shell ${activeView === "reports" ? "reports-shell" : ""}`}>
        <header className="chat-header">
          <div className="brand">
            <span className="brand-dot" />
            <div>
              <h1>Bússola da Sustentabilidade</h1>
              <p>{activeView === "chat" ? "Assistente de análise de dados" : "Geração e validação de relatórios"}</p>
            </div>
          </div>
          <div className="header-actions">
            <div className="view-tabs" role="tablist" aria-label="Alternar área do sistema">
              <button type="button" className={activeView === "chat" ? "active" : ""} onClick={() => setActiveView("chat")}>Chat</button>
              <button type="button" className={activeView === "reports" ? "active" : ""} onClick={() => setActiveView("reports")}>Relatórios</button>
            </div>
            <button type="button" className="theme-btn" onClick={toggleTheme} aria-label="Alternar tema">
              {theme === "dark" ? <FiSun size={25} /> : <FiMoon size={25} />}
            </button>
            {activeView === "chat" && (
              <button type="button" onClick={clearChat} className="ghost-btn" aria-label="Nova conversa">
                <CiCirclePlus size={30} />
              </button>
            )}
          </div>
        </header>

        {activeView === "reports" ? (
          <ReportWorkspace />
        ) : (
          <>
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
                  const isAssistantStreaming = isStreaming && msg.role === "assistant" && msg.id === activeAssistantId;
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
          </>
        )}
      </div>
    </div>
  );
}
