"""
Question-bank storage abstraction.

Why a repository layer?
The production database is owned by another teammate. AI logic must not
import PostgreSQL/MySQL/MongoDB drivers. Stage 10 will add an in-memory /
JSON implementation of QuestionBankRepository. Later they implement the
same interface against their database.
"""
