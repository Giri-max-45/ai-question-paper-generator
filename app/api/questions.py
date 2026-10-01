"""Question generation/validation endpoints. Logic arrives in Stages 6–9."""

from fastapi import APIRouter

from app.models.common import StageNotReadyResponse
from app.models.question import (
    DuplicateCheckRequest,
    GenerateQuestionsRequest,
    ValidateQuestionRequest,
)

router = APIRouter(prefix="/questions", tags=["questions"])


@router.post(
    "/generate",
    response_model=StageNotReadyResponse,
    summary="Generate questions from retrieved syllabus context (RAG + LLM)",
)
def generate_questions(_body: GenerateQuestionsRequest) -> StageNotReadyResponse:
    return StageNotReadyResponse(
        endpoint="POST /questions/generate",
        message="Stages 5–6 will retrieve context and call the LLM with structured JSON output.",
    )


@router.post(
    "/validate",
    response_model=StageNotReadyResponse,
    summary="Validate a question against syllabus, clarity, marks, and duplicates",
)
def validate_question(_body: ValidateQuestionRequest) -> StageNotReadyResponse:
    return StageNotReadyResponse(
        endpoint="POST /questions/validate",
        message="Stage 9 will return is_valid plus per-check flags.",
    )


@router.post(
    "/check-duplicate",
    response_model=StageNotReadyResponse,
    summary="Semantic duplicate detection using cosine similarity",
)
def check_duplicate(_body: DuplicateCheckRequest) -> StageNotReadyResponse:
    return StageNotReadyResponse(
        endpoint="POST /questions/check-duplicate",
        message="Stage 8 will compare embeddings and return a similarity score.",
    )
