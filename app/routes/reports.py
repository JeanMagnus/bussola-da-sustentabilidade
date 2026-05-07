import base64
from datetime import datetime, timezone
from io import BytesIO
from textwrap import wrap
from typing import Literal
from uuid import uuid4

import fitz
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field

router = APIRouter(prefix="/reports", tags=["Reports"])

TEMPLATES = [
    {
        "id": "sustainability-summary",
        "name": "Resumo Executivo Sustentável",
        "description": "Relatório objetivo para apresentar indicadores, achados e recomendações de sustentabilidade.",
        "accent": "#CC0033",
        "background": "#FFF7F8",
    },
    {
        "id": "comparative-analysis",
        "name": "Análise Comparativa Municipal",
        "description": "Template para comparar destinos, critérios, evolução temporal e pontos de atenção.",
        "accent": "#2563EB",
        "background": "#F7FAFF",
    },
    {
        "id": "validation-briefing",
        "name": "Briefing para Validação",
        "description": "Modelo enxuto para enviar conclusões a um validador antes da publicação final.",
        "accent": "#047857",
        "background": "#F4FBF7",
    },
]

REPORTS: dict[str, dict] = {}


class ReportCreate(BaseModel):
    template_id: str = Field(..., min_length=1)
    requested_by: str = Field(..., min_length=2, max_length=120)
    validator: str = Field(..., min_length=2, max_length=120)
    instructions: str = Field(..., min_length=12, max_length=4000)


class ReportValidation(BaseModel):
    decision: Literal["approved", "rejected"]
    notes: str = Field(default="", max_length=1000)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _get_template(template_id: str) -> dict:
    for template in TEMPLATES:
        if template["id"] == template_id:
            return template
    raise HTTPException(status_code=404, detail="Template de relatório não encontrado.")


def _hex_to_rgb(hex_color: str) -> tuple[float, float, float]:
    value = hex_color.lstrip("#")
    return tuple(int(value[index:index + 2], 16) / 255 for index in (0, 2, 4))


def _insert_wrapped_text(page, text: str, x: float, y: float, max_chars: int, line_height: float, **kwargs) -> float:
    for paragraph in text.split("\n"):
        lines = wrap(paragraph.strip(), width=max_chars) or [""]
        for line in lines:
            page.insert_text((x, y), line, **kwargs)
            y += line_height
        y += line_height * 0.35
    return y


def _draft_report_text(instructions: str, template_name: str) -> dict[str, str]:
    cleaned = " ".join(instructions.split())
    highlights = [part.strip(" .") for part in cleaned.replace(";", ".").split(".") if part.strip()]
    highlights = highlights[:4] or [cleaned]

    bullets = "\n".join(f"• {item}" for item in highlights)
    return {
        "title": f"Relatório - {template_name}",
        "summary": (
            "Este relatório foi preenchido pelo agente a partir das informações solicitadas pelo usuário. "
            "O conteúdo abaixo organiza o pedido em formato executivo para revisão, validação e posterior emissão em PDF."
        ),
        "requested_content": cleaned,
        "highlights": bullets,
        "recommendations": (
            "• Validar se os indicadores e municípios citados estão corretos.\n"
            "• Conferir se há dados sensíveis ou conclusões que exigem ajuste de linguagem.\n"
            "• Aprovar apenas quando o relatório estiver pronto para download pelo solicitante."
        ),
    }


def _create_pdf(template: dict, payload: ReportCreate, report_id: str) -> bytes:
    accent = _hex_to_rgb(template["accent"])
    doc = fitz.open()
    page = doc.new_page(width=595, height=842)
    report_text = _draft_report_text(payload.instructions, template["name"])

    page.draw_rect(fitz.Rect(0, 0, 595, 842), color=None, fill=_hex_to_rgb(template["background"]))
    page.draw_rect(fitz.Rect(0, 0, 595, 96), color=None, fill=accent)
    page.draw_rect(fitz.Rect(44, 132, 551, 790), color=(0.9, 0.9, 0.9), fill=(1, 1, 1))
    page.draw_line((44, 190), (551, 190), color=accent, width=1.4)

    page.insert_text((48, 45), "Bússola da Sustentabilidade", fontsize=18, color=(1, 1, 1), fontname="helv")
    page.insert_text((48, 70), template["name"], fontsize=11, color=(1, 1, 1), fontname="helv")
    page.insert_text((64, 162), report_text["title"], fontsize=18, color=accent, fontname="helv")

    meta = f"Solicitante: {payload.requested_by}  |  Validador: {payload.validator}  |  ID: {report_id[:8]}"
    page.insert_text((64, 184), meta, fontsize=8.5, color=(0.34, 0.36, 0.40), fontname="helv")

    y = 225
    sections = [
        ("Síntese gerada pelo agente", report_text["summary"]),
        ("Informações solicitadas pelo usuário", report_text["requested_content"]),
        ("Pontos de destaque", report_text["highlights"]),
        ("Checklist para validação", report_text["recommendations"]),
    ]

    for heading, content in sections:
        if y > 720:
            page = doc.new_page(width=595, height=842)
            page.draw_rect(fitz.Rect(0, 0, 595, 842), color=None, fill=_hex_to_rgb(template["background"]))
            page.draw_rect(fitz.Rect(44, 52, 551, 790), color=(0.9, 0.9, 0.9), fill=(1, 1, 1))
            y = 92
        page.insert_text((64, y), heading, fontsize=12, color=accent, fontname="helv")
        y = _insert_wrapped_text(page, content, 64, y + 22, 82, 13, fontsize=9.5, color=(0.16, 0.18, 0.22), fontname="helv") + 10

    for page_number, pdf_page in enumerate(doc, start=1):
        pdf_page.insert_text((64, 814), f"Prévia controlada • Página {page_number} • Download liberado somente após aprovação", fontsize=8, color=(0.48, 0.48, 0.48), fontname="helv")

    output = BytesIO()
    doc.save(output)
    doc.close()
    return output.getvalue()


def _preview_pages(pdf_bytes: bytes) -> list[str]:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    pages: list[str] = []
    for page in doc:
        pix = page.get_pixmap(matrix=fitz.Matrix(0.9, 0.9), alpha=False)
        pages.append(f"data:image/png;base64,{base64.b64encode(pix.tobytes('png')).decode('ascii')}")
    doc.close()
    return pages


def _public_report(record: dict, include_preview: bool = False) -> dict:
    payload = {key: value for key, value in record.items() if key not in {"pdf_bytes", "preview_pages"}}
    if include_preview:
        payload["preview_pages"] = record["preview_pages"]
    return payload


@router.get("/templates")
async def list_templates():
    return {"templates": TEMPLATES}


@router.post("")
async def create_report(payload: ReportCreate):
    template = _get_template(payload.template_id)
    report_id = str(uuid4())
    pdf_bytes = _create_pdf(template, payload, report_id)
    record = {
        "id": report_id,
        "template": template,
        "requested_by": payload.requested_by,
        "validator": payload.validator,
        "instructions": payload.instructions,
        "status": "pending_validation",
        "status_label": "Aguardando validação",
        "validator_notes": "",
        "created_at": _now_iso(),
        "updated_at": _now_iso(),
        "pdf_bytes": pdf_bytes,
        "preview_pages": _preview_pages(pdf_bytes),
    }
    REPORTS[report_id] = record
    return _public_report(record, include_preview=True)


@router.get("")
async def list_reports(validator: str | None = None):
    reports = REPORTS.values()
    if validator:
        reports = [report for report in reports if report["validator"].lower() == validator.lower()]
    return {"reports": [_public_report(report) for report in reports]}


@router.get("/{report_id}")
async def get_report(report_id: str):
    record = REPORTS.get(report_id)
    if not record:
        raise HTTPException(status_code=404, detail="Relatório não encontrado.")
    return _public_report(record, include_preview=True)


@router.patch("/{report_id}/validation")
async def validate_report(report_id: str, payload: ReportValidation):
    record = REPORTS.get(report_id)
    if not record:
        raise HTTPException(status_code=404, detail="Relatório não encontrado.")

    record["status"] = payload.decision
    record["status_label"] = "Aprovado para download" if payload.decision == "approved" else "Reprovado pelo validador"
    record["validator_notes"] = payload.notes
    record["updated_at"] = _now_iso()
    return _public_report(record, include_preview=True)


@router.get("/{report_id}/download")
async def download_report(report_id: str):
    record = REPORTS.get(report_id)
    if not record:
        raise HTTPException(status_code=404, detail="Relatório não encontrado.")
    if record["status"] != "approved":
        raise HTTPException(status_code=403, detail="Download bloqueado até a aprovação do validador.")

    filename = f"relatorio-bussola-{report_id[:8]}.pdf"
    return Response(
        content=record["pdf_bytes"],
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
