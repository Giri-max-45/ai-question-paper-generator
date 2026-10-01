# AI-Based Smart Question Paper Generator — AI Module

Standalone **FastAPI microservice**. This repo is **only the AI service**.

- Do **not** build the college frontend here.
- Do **not** build the main application backend here.
- Do **not** couple AI logic to PostgreSQL/MySQL/MongoDB.

Teammates integrate by calling REST APIs with JSON.

Current milestone: **Stage 1 — project structure + FastAPI server**.

---

## 1. Architecture (for viva)

```
[ Students / Faculty UI ]          ← teammate: frontend
           |
           v
[ Main Backend API + Auth + DB ]   ← teammates: backend + database
           |
           |  HTTP JSON  (this contract)
           v
[ THIS SERVICE: FastAPI AI Module ]
           |
           +-- PDF extract (PyMuPDF)
           +-- Clean + chunk text
           +-- Topics / modules (NLP + LLM)
           +-- Embeddings (Sentence Transformers)
           +-- Vector search (FAISS)  → RAG context
           +-- LLM question generation (swappable provider)
           +-- Difficulty + Bloom classification
           +-- Semantic duplicate check
           +-- Validation (syllabus-bound)
           +-- Paper assembly (exact marks)
           +-- QuestionBankRepository (in-memory/JSON now; their DB later)
```

**Data flow (full pipeline, later stages):**

PDF/Syllabus/Notes → extract → clean → modules/topics → chunks → embeddings → vector DB → retrieve (RAG) → LLM questions → difficulty/Bloom → validate → de-duplicate → select by exam pattern → question paper JSON.

AI output is **reviewable**. The service returns validation flags. Humans should approve questions before publishing.

---

## 2. Why each technology?

| Technology | Why we use it |
|------------|----------------|
| **Python 3.11+** | Standard language for NLP/ML college projects; FastAPI ecosystem. |
| **FastAPI** | REST APIs + automatic `/docs`. Easy for any backend (Node, Spring, Django) to call. |
| **Uvicorn** | ASGI server that runs FastAPI. |
| **Pydantic** | Validates LLM JSON and HTTP bodies. Rejects malformed output. |
| **python-dotenv** | API keys stay out of source code. |
| **PyMuPDF** (Stage 2) | Reliable PDF text + page numbers. |
| **spaCy / NLTK** (Stage 3) | Headings, sentences, light NLP without calling the LLM for everything. |
| **Sentence Transformers** (Stage 4) | Turn text into vectors so “similar meaning” can be measured. |
| **FAISS** (Stage 4) | Fast similarity search over those vectors (RAG + duplicates). |
| **LLM API** (Stage 6) | Generate exam-style questions from **retrieved** syllabus text only. Provider is abstracted. |
| **pytest** | Automated tests for marks math, duplicates, API health. |

**Why RAG?** An LLM alone may invent topics not in the syllabus. RAG first retrieves chunks from *your* PDFs, then asks the model to write questions **only from that context**.

**Why embeddings?** Computers compare meaning using vectors, not exact strings. “Advantages of normalization” vs “benefits of database normalization” become close vectors.

---

## 3. Folder structure

```
ai_question_generator/
├── app/
│   ├── main.py              # FastAPI app
│   ├── config.py            # Settings from .env
│   ├── api/                 # HTTP routes (thin)
│   ├── models/              # Pydantic contracts
│   ├── services/            # AI pipeline (filled stage by stage)
│   ├── repositories/        # Abstract question bank
│   ├── prompts/             # LLM prompt files (later)
│   └── utils/
├── data/sample/             # Example exam pattern
├── data/uploads/            # Uploaded PDFs (later)
├── tests/
├── run.py
├── requirements.txt
└── .env.example
```

---

## 4. Stage 1 — install and run (Windows PowerShell)

You need **Python 3.11 or newer**. Check:

```powershell
python --version
```

From this project folder:

```powershell
cd C:\Users\giris\Projects\ai_question_generator

python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

copy .env.example .env

python run.py
```

Open:

- Health: http://127.0.0.1:8000/health
- Swagger UI: http://127.0.0.1:8000/docs

If `Activate.ps1` is blocked:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### Tests

```powershell
pytest -q
```

### Sample health request

```powershell
curl.exe -X POST http://127.0.0.1:8000/health
```

Expected JSON:

```json
{
  "status": "ok",
  "service": "AI Question Generator",
  "version": "0.1.0",
  "stage": "stage_1_fastapi_server",
  "message": "AI service is running. Later stages (PDF, RAG, LLM) are not wired yet."
}
```

Other endpoints exist in `/docs` but return `"implemented": false` until their stage.

---

## 5. How the team's backend will integrate

1. Run this service on a port (example: `8000`).
2. Backend sends HTTP requests (form-data for PDFs, JSON for generation).
3. Backend stores returned `question` / `paper_id` in **their** database.
4. Frontend never needs to talk to the LLM directly.

Example later call (Stage 6):

`POST http://127.0.0.1:8000/questions/generate` with JSON body `{ "subject": "DBMS", ... }`.

Auth, users, and PostgreSQL stay on their backend.

---

## 6. Development stages

| Stage | Status | What |
|-------|--------|------|
| 1 | **You are here** | Structure + FastAPI + health |
| 2 | Next | PDF extraction |
| 3 | | Syllabus topics |
| 4 | | Embeddings + FAISS |
| 5 | | RAG retrieval |
| 6 | | LLM question generation |
| 7 | | Difficulty + Bloom |
| 8 | | Duplicate detection |
| 9 | | Validation |
| 10 | | Paper generation + marks |
| 11 | | Previous-paper analysis |
| 12 | | Full integration guide |

We implement **one stage at a time** and keep it runnable.

---

## 7. Honest limitations (say this in viva)

- Difficulty and Bloom labels are **AI estimates**, not exact science.
- Scanned PDFs without OCR may have empty text.
- LLM may still err; validation + human review are required.
- Stage 1 cannot generate questions yet.
