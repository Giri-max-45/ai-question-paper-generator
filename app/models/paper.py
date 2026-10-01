"""Examination pattern and question-paper models. Assembly arrives in Stage 10."""

from typing import Optional

from pydantic import BaseModel, Field

from app.models.question import Difficulty, Question


class PaperSectionConfig(BaseModel):
    name: str = Field(examples=["Section A"])
    number_of_questions: int = Field(ge=1)
    marks_per_question: int = Field(ge=1)
    question_type: Optional[str] = None


class DifficultyDistribution(BaseModel):
    """Percentages. They should add up to 100; Stage 10 will validate this."""

    easy: int = Field(ge=0, le=100, examples=[30])
    medium: int = Field(ge=0, le=100, examples=[50])
    hard: int = Field(ge=0, le=100, examples=[20])


class ExamPattern(BaseModel):
    subject: str = Field(examples=["DBMS"])
    total_marks: int = Field(ge=1, examples=[70])
    duration_minutes: int = Field(ge=1, examples=[180])
    difficulty_distribution: DifficultyDistribution
    sections: list[PaperSectionConfig]
    modules: Optional[list[str]] = None


class PaperSection(BaseModel):
    name: str
    questions: list[Question]
    section_marks: int


class PaperValidation(BaseModel):
    marks_valid: bool
    module_coverage_valid: bool
    duplicate_free: bool
    notes: Optional[str] = Field(
        default=None,
        description="AI output is reviewed by humans before publishing.",
    )


class QuestionPaper(BaseModel):
    paper_id: str
    subject: str
    total_marks: int
    duration_minutes: int
    sections: list[PaperSection]
    validation: PaperValidation


class GeneratePaperRequest(ExamPattern):
    """Same shape as the exam pattern, plus optional extra constraints later."""

    pass
