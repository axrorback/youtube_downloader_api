from fastapi import FastAPI
from app.routes import youtube

app = FastAPI(
    title="YouTube Downloader API",
    description="🎥 YouTube videolarini va audiolarini yuklab olish uchun API",
    version="1.0.0",
)
@app.get("/")
def root():
    return {"message": "YouTube Downloader API ishlayapti 🚀"}

# Routes
app.include_router(youtube.router, prefix="/youtube", tags=["YouTube"])
