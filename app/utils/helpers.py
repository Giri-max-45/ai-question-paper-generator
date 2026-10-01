"""Utility helpers used from Stage 1 onward."""

from fastapi import HTTPException, status

from app.models.common import ErrorResponse


def http_error(status_code: int, error_code: str, message: str, details: dict | None = None) -> None:
    """Raise a FastAPI HTTPException with a consistent JSON body."""
    payload = ErrorResponse(error_code=error_code, message=message, details=details)
    raise HTTPException(status_code=status_code, detail=payload.model_dump())


def not_implemented(endpoint: str, stage: str) -> None:
    http_error(
        status.HTTP_501_NOT_IMPLEMENTED,
        error_code="STAGE_NOT_READY",
        message=f"{endpoint} will be implemented in {stage}.",
    )
