from fastapi import FastAPI

app = FastAPI(
    title="QazaqGuide AI API",
    description="Backend API for QazaqGuide AI",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to QazaqGuide AI 🇰🇿"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }