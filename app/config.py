"""
Application settings.

Why python-dotenv / pydantic-settings?
- Teammates will later pass secrets (LLM API keys) without putting them in code.
- Settings are loaded from a `.env` file in development.
- If a required key is missing later (Stage 6+), we can fail with a clear error.
"""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


# Project root: .../ai_question_generator
PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """All configurable values live here so nothing is hard-coded in services."""

    model_config = SettingsConfigDict(
        env_file=str(PROJECT_ROOT / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "AI Question Generator"
    app_version: str = "0.1.0"
    debug: bool = True

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # Folders used in later stages
    data_dir: Path = PROJECT_ROOT / "data"
    upload_dir: Path = PROJECT_ROOT / "data" / "uploads"
    sample_dir: Path = PROJECT_ROOT / "data" / "sample"

    # Duplicate detection (Stage 8) — configurable as requested
    duplicate_threshold: float = 0.85

    # LLM (used from Stage 6). Empty is OK in Stage 1.
    llm_provider: str = "openai_compatible"
    llm_api_key: str = ""
    llm_base_url: str = "https://api.openai.com/v1"
    llm_model: str = "gpt-4o-mini"

    # Embeddings (Stage 4)
    embedding_model: str = "all-MiniLM-L6-v2"


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings object so we do not re-read .env on every request."""
    settings = Settings()
    settings.upload_dir.mkdir(parents=True, exist_ok=True)
    settings.sample_dir.mkdir(parents=True, exist_ok=True)
    return settings
