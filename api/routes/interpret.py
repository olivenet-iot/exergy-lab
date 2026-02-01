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
    compressor_type: str = ""          # backward compat
    equipment_type: str = "compressor"
    subtype: str = ""
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
        # Resolve equipment_type and subtype (backward compat: fall back to compressor_type)
        equipment_type = request.equipment_type
        subtype = request.subtype or request.compressor_type

        interpretation = await interpret_with_claude_code(
            analysis_result=request.analysis_result,
            equipment_type=equipment_type,
            subtype=subtype,
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
