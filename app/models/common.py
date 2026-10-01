"""Shared API models used by every endpoint."""

from typing import Any, Optional

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(examples=["ok"])
    service: str
    version: str
    stage: str
    message: str


class ErrorResponse(BaseModel):
    """Standard error body returned to the team's backend."""

    error_code: str = Field(
        description="Machine-readable code, e.g. INVALID_PDF, MISSING_API_KEY"
    )
    message: str
    details: Optional[dict[str, Any]] = None


class StageNotReadyResponse(BaseModel):
    """Returned until a later development stage implements the real logic."""

    implemented: bool = False
    current_stage: str = "stage_1"
    endpoint: str
    message: str
