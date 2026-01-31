"""Interpretation routes for ExergyLab API."""

import logging
from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

from api.services.claude_code_service import interpret_with_claude_code

logger = logging.getLogger(__name__)

router = APIRouter()


class InterpretRequest(BaseModel):
    analysis_result: dict[str, Any]
    compressor_type: str
    parameters: dict[str, Any]


class InterpretResponse(BaseModel):
    success: bool
    interpretation: dict[str, Any]


@router.post("/interpret", response_model=InterpretResponse)
async def interpret(request: InterpretRequest):
    """AI-powered interpretation of exergy analysis results.

    Never raises to client — always returns a valid response.
    If AI fails, interpretation.ai_available will be False.
    """
    try:
        interpretation = await interpret_with_claude_code(
            analysis_result=request.analysis_result,
            compressor_type=request.compressor_type,
            parameters=request.parameters,
        )
        return InterpretResponse(success=True, interpretation=interpretation)
    except Exception:
        logger.exception("Unexpected error in interpret endpoint")
        return InterpretResponse(
            success=False,
            interpretation={
                "ai_available": False,
                "summary": "",
                "detailed_analysis": "",
                "key_insights": [],
                "recommendations": [],
                "not_recommended": [],
                "action_plan": {"immediate": [], "short_term": [], "medium_term": []},
                "warnings": [],
            },
        )
