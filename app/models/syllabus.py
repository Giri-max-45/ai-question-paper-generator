"""Syllabus and topic models. Extraction logic arrives in Stage 3."""

from typing import Optional

from pydantic import BaseModel, Field


class SyllabusModule(BaseModel):
    module: str = Field(examples=["Module 3"])
    title: Optional[str] = Field(default=None, examples=["Database Design"])
    topics: list[str] = Field(default_factory=list)
    subtopics: list[str] = Field(default_factory=list)
    important_concepts: list[str] = Field(default_factory=list)


class SyllabusAnalysis(BaseModel):
    subject: Optional[str] = None
    modules: list[SyllabusModule] = Field(default_factory=list)
    source_file: Optional[str] = None


class TopicExtractRequest(BaseModel):
    text: Optional[str] = Field(
        default=None,
        description="Raw syllabus text. If omitted, use a previously processed document id.",
    )
    document_id: Optional[str] = None
