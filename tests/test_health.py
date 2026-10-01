"""Stage 1 tests: server boots and health endpoints work."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_get():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["stage"] == "stage_1_fastapi_server"


def test_health_post():
    response = client.post("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_openapi_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200


def test_generate_questions_is_stubbed():
    """Until Stage 6, the contract exists but logic is not ready."""
    response = client.post(
        "/questions/generate",
        json={
            "subject": "DBMS",
            "module": "Module 3",
            "topic": "Normalization",
            "number_of_questions": 5,
            "marks": 10,
            "difficulty": "hard",
            "question_type": "long_answer",
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["implemented"] is False
    assert "POST /questions/generate" in body["endpoint"]
