"""Abstract question-bank interface (no production DB coupling)."""

from abc import ABC, abstractmethod
from typing import Optional

from app.models.paper import QuestionPaper
from app.models.question import Question


class QuestionBankRepository(ABC):
    """Swap this for PostgreSQL later without changing services."""

    @abstractmethod
    def save_question(self, question: Question) -> Question:
        raise NotImplementedError

    @abstractmethod
    def list_questions(self, subject: Optional[str] = None) -> list[Question]:
        raise NotImplementedError

    @abstractmethod
    def save_paper(self, paper: QuestionPaper) -> QuestionPaper:
        raise NotImplementedError

    @abstractmethod
    def get_paper(self, paper_id: str) -> Optional[QuestionPaper]:
        raise NotImplementedError
