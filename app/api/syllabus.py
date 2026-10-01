"""Syllabus analysis endpoints. Real NLP extraction is Stage 3."""

from fastapi import APIRouter

from app.models.common import StageNotReadyResponse
from app.models.syllabus import TopicExtractRequest

router = APIRouter(tags=["syllabus"])


@router.post(
    "/syllabus/analyze",
    response_model=StageNotReadyResponse,
    summary="Analyze a syllabus into modules, topics, and subtopics",
)
def analyze_syllabus() -> StageNotReadyResponse:
    return StageNotReadyResponse(
        endpoint="POST /syllabus/analyze",
        message="Stage 3 will detect modules/topics and preserve parent-child relationships.",
    )


@router.post(
    "/topics/extract",
    response_model=StageNotReadyResponse,
    summary="Extract topics/subtopics from syllabus text",
)
def extract_topics(_body: TopicExtractRequest) -> StageNotReadyResponse:
    return StageNotReadyResponse(
        endpoint="POST /topics/extract",
        message="Stage 3 will return structured JSON similar to the Module 3 Normalization example.",
    )
