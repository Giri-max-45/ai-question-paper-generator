"""Question-related API models. Full generation logic arrives in Stages 6–9."""

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Difficulty(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


class QuestionType(str, Enum):
    short_answer = "short_answer"
    long_answer = "long_answer"
    mcq = "mcq"
    numerical = "numerical"
    conceptual = "conceptual"
    application = "application"
    case_based = "case_based"


class BloomLevel(str, Enum):
    remember = "Remember"
    understand = "Understand"
    apply = "Apply"
    analyze = "Analyze"
    evaluate = "Evaluate"
    create = "Create"


class Question(BaseModel):
    """One examination-ready question. Human review is still required."""

    id: str
    question: str
    type: QuestionType
    marks: int = Field(ge=1)
    difficulty: Difficulty
    module: Optional[str] = None
    topic: Optional[str] = None
    subtopic: Optional[str] = None
    learning_level: Optional[BloomLevel] = None
    options: Optional[list[str]] = None
    answer_key: Optional[str] = Field(
        default=None,
        description="Optional model answer / MCQ key. Review before publishing.",
    )


class GenerateQuestionsRequest(BaseModel):
    subject: str = Field(examples=["DBMS"])
    module: Optional[str] = Field(default=None, examples=["Module 3"])
    topic: Optional[str] = Field(default=None, examples=["Normalization"])
    number_of_questions: int = Field(default=5, ge=1, le=50)
    marks: int = Field(default=10, ge=1)
    difficulty: Optional[Difficulty] = None
    question_type: Optional[QuestionType] = None


class GenerateQuestionsResponse(BaseModel):
    questions: list[Question]


class ValidationResult(BaseModel):
    is_valid: bool
    syllabus_relevant: bool
    clear: bool
    duplicate: bool
    difficulty_valid: bool
    reason: Optional[str] = None


class ValidateQuestionRequest(BaseModel):
    question: Question
    subject: Optional[str] = None


class DuplicateCheckRequest(BaseModel):
    question_a: str
    question_b: str
    threshold: Optional[float] = Field(
        default=None,
        description="Override DUPLICATE_THRESHOLD if provided",
    )


class DuplicateCheckResponse(BaseModel):
    similar: bool
    similarity_score: float
    threshold: float
