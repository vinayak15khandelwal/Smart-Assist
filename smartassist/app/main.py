from fastapi import FastAPI

from app.routes import chat

app = FastAPI(
    title="SmartAssist",
    description="AI-powered customer support chatbot",
    version="0.1.0",
)

app.include_router(chat.router)


@app.get("/health")
def health():
    return {"status": "ok"}
