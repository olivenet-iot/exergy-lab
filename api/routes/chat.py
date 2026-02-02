"""Chat routes for ExergyLab AI knowledge-powered chat."""

import logging
from typing import Any, List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.services.claude_code_service import ClaudeCodeClient

logger = logging.getLogger(__name__)

router = APIRouter()


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    equipment_type: str
    subtype: Optional[str] = None
    question: str
    analysis_data: Optional[dict[str, Any]] = None
    history: Optional[List[ChatMessage]] = None


class ChatResponse(BaseModel):
    answer: str
    knowledge_sources: List[str]
    follow_up_suggestions: List[str]
    ai_available: bool


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Knowledge-powered AI chat endpoint.

    Accepts a user question alongside optional analysis context and conversation
    history, routes to relevant knowledge files, and returns an AI-generated
    Turkish-language answer.
    """
    if not request.question or not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        history_dicts = None
        if request.history:
            history_dicts = [msg.model_dump() for msg in request.history]

        client = ClaudeCodeClient.get_instance()
        result = await client.chat(
            equipment_type=request.equipment_type,
            subtype=request.subtype,
            question=request.question.strip(),
            analysis_data=request.analysis_data,
            history=history_dicts,
        )

        return ChatResponse(
            answer=result.get("answer", ""),
            knowledge_sources=result.get("knowledge_sources", []),
            follow_up_suggestions=result.get("follow_up_suggestions", []),
            ai_available=result.get("ai_available", False),
        )

    except Exception:
        logger.exception("Unexpected error in chat endpoint")
        return ChatResponse(
            answer="Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin.",
            knowledge_sources=[],
            follow_up_suggestions=[],
            ai_available=False,
        )
