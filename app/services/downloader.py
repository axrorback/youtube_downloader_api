import yt_dlp

def get_formats(url: str):
    """Berilgan URL uchun mavjud formatlarni qaytaradi"""
    ydl_opts = {"quiet": True, "skip_download": True}
    formats = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        for f in info.get("formats", []):
            formats.append({
                "format_id": f.get("format_id"),
                "ext": f.get("ext"),
                "resolution": f.get("resolution") or f.get("height"),
                "filesize": f.get("filesize"),
                "fps": f.get("fps"),
                "vcodec": f.get("vcodec"),
                "acodec": f.get("acodec"),
            })
    return {"title": info.get("title"), "formats": formats}

def download_video(url: str, format_id: str):
    """Video yoki audio yuklab beradi"""
    ydl_opts = {
        "format": format_id,
        "outtmpl": "downloads/%(title)s.%(ext)s",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    return {"status": "success", "file": filename, "title": info.get("title")}
