"""Document upload/process endpoints. Real PDF work is Stage 2."""

from fastapi import APIRouter, File, UploadFile

from app.models.common import StageNotReadyResponse

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post(
    "/upload",
    response_model=StageNotReadyResponse,
    summary="Upload syllabus / notes / previous paper PDF",
)
async def upload_document(file: UploadFile = File(...)) -> StageNotReadyResponse:
    return StageNotReadyResponse(
        endpoint="POST /documents/upload",
        message=(
            f"Received filename '{file.filename}' but Stage 2 (PDF extraction) "
            "is not implemented yet. The file was not stored."
        ),
    )


@router.post(
    "/process",
    response_model=StageNotReadyResponse,
    summary="Extract and clean text from an uploaded PDF",
)
def process_document() -> StageNotReadyResponse:
    return StageNotReadyResponse(
        endpoint="POST /documents/process",
        message="Stage 2 will extract text with PyMuPDF, clean it, and attach page metadata.",
    )
