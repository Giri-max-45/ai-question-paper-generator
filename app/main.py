"""
FastAPI application entry point (Stage 1).

Why FastAPI?
- Automatic OpenAPI docs at /docs (useful for teammates and viva).
- Pydantic validates every request/response (fewer silent bugs).
- Async-ready HTTP APIs that a Node/Java/Python backend can call later.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import documents, papers, questions, syllabus
from app.config import get_settings
from app.models.common import ErrorResponse, HealthResponse

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "Standalone AI microservice for syllabus understanding, "
        "question generation, validation, and question-paper assembly. "
        "Your team's frontend/backend/database should call these REST APIs. "
        "Do not couple this service to a specific production database."
    ),
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS: allow the team's backend/frontend during local development.
# In production they can restrict origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/health",
    response_model=HealthResponse,
    tags=["health"],
    summary="Health check (GET)",
)
@app.post(
    "/health",
    response_model=HealthResponse,
    tags=["health"],
    summary="Health check (POST)",
    responses={500: {"model": ErrorResponse}},
)
def health_check() -> HealthResponse:
    """Simple liveness check so teammates can verify the AI service is running."""
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        version=settings.app_version,
        stage="stage_1_fastapi_server",
        message="AI service is running. Later stages (PDF, RAG, LLM) are not wired yet.",
    )


# Routers for later stages. Stage 1 registers them so /docs shows the full contract.
app.include_router(documents.router)
app.include_router(syllabus.router)
app.include_router(questions.router)
app.include_router(papers.router)
