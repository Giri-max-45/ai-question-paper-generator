"""Question-paper and previous-paper endpoints. Stages 10–11."""

from fastapi import APIRouter

from app.models.common import StageNotReadyResponse
from app.models.paper import GeneratePaperRequest

router = APIRouter(tags=["papers"])


@router.post(
    "/question-paper/generate",
    response_model=StageNotReadyResponse,
    summary="Assemble a balanced question paper with exact total marks",
)
def generate_paper(_body: GeneratePaperRequest) -> StageNotReadyResponse:
    return StageNotReadyResponse(
        endpoint="POST /question-paper/generate",
        message="Stage 10 will select questions to match sections, marks, difficulty, and coverage.",
    )


@router.get(
    "/question-paper/{paper_id}",
    response_model=StageNotReadyResponse,
    summary="Fetch a previously generated paper by id",
)
def get_paper(paper_id: str) -> StageNotReadyResponse:
    return StageNotReadyResponse(
        endpoint="GET /question-paper/{paper_id}",
        message=f"Stage 10 will load paper '{paper_id}' from the abstract question-bank store.",
    )


@router.post(
    "/previous-papers/analyze",
    response_model=StageNotReadyResponse,
    summary="Analyze previous papers for topic frequency (do not copy questions)",
)
def analyze_previous_papers() -> StageNotReadyResponse:
    return StageNotReadyResponse(
        endpoint="POST /previous-papers/analyze",
        message="Stage 11 will report frequently tested topics without copying old questions.",
    )
