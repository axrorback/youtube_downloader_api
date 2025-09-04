from fastapi import FastAPI
from app.routes import youtube

app = FastAPI(
    title="YouTube Downloader API",
    description="🎥 YouTube videolarini va audiolarini yuklab olish uchun API",
    version="1.0.0",
)

# Routes
app.include_router(youtube.router, prefix="/youtube", tags=["YouTube"])
