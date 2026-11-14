# SmartAssist

AI-powered customer support chatbot. Understands user intent, retrieves relevant
knowledge base articles (RAG), generates contextual answers with an LLM, keeps
conversation memory, and escalates to a human when needed.

**Planned stack:** Python, FastAPI, spaCy, sentence-transformers, ChromaDB,
Gemini/OpenAI API, SQLite, Docker.

## Run locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive API docs.

## Test

```bash
pytest
```

## Progress

- [x] Day 1: project setup, FastAPI skeleton, `/chat` echo endpoint
