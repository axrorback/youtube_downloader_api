from fastapi import APIRouter
from app.schemas.youtube import VideoRequest, DownloadRequest
from app.services.downloader import get_formats, download_video

router = APIRouter()

@router.post("/formats")
async def list_formats(request: VideoRequest):
    return get_formats(request.url)

@router.post("/download")
async def download(request: DownloadRequest):
    return download_video(request.url, request.format_id)
