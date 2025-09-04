# 🎥 YouTube Downloader API

[![CI](https://github.com/axrorback/youtube-downloader-api/actions/workflows/ci.yml/badge.svg)](https://github.com/axrorback/youtube-downloader-api/actions/workflows/python-app.yml)

`FastAPI` va `yt-dlp` yordamida qurilgan **YouTube video/audio yuklab olish API**.
Swagger hujjatlashuvi, Postman testlari va Telegram bot integratsiyasi uchun tayyor.

---

## ✨ Xususiyatlari

* 📺 **Video yuklab olish** (istalgan sifat va formatda)
* 🎷 **Audio (mp3/mp4a) yuklab olish**
* 📂 **Formatlarni ko‘rsatish** (resolution, codec, ext va h.k.)
* ⚡ **StreamingResponse** orqali katta fayllarni oqim bilan berish
* 🔗 **Download link** berish imkoniyati (Telegram bot integratsiyasi uchun qulay)
* 📝 **Swagger Docs** avtomatik hujjatlashuv

---

## 📂 Loyihaning Strukturasi

```
youtube_downloader_api/
│── app/
│   ├── main.py             # FastAPI ilovasi kirish nuqtasi
│   ├── config.py           # Sozlamalar
│   ├── routes/
│   │   └── youtube.py      # API marshrutlari
│   ├── services/
│   │   └── downloader.py   # Video/audio yuklab olish logikasi
│   ├── schemas/
│   │   └── youtube.py      # Pydantic modellari
│   └── utils/              # Qo‘shimcha yordamchi funksiyalar
│
├── requirements.txt        # Kerakli kutubxonalar
└── README.md               # Loyihaning qisqacha tavsifi
```

---

## ⚙️ O‘rnatish

```bash
# Repository'ni clone qilish
git clone https://github.com/axrorback/youtube-downloader-api.git
cd youtube-downloader-api

# Virtual environment yaratish
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

# Kutubxonalarni o‘rnatish
pip install -r requirements.txt
```

---

## 🚀 Ishga tushirish

```bash
uvicorn app.main:app --reload
```

Ilova default bo‘yicha quyida ishlaydi:

```
http://127.0.0.1:8000
```

---

## 📌 Endpointlar

### 🔹 1. API Status

**GET** `/`

API ishlayotganini tekshirish uchun.

---

### 🔹 2. Formatlarni olish

**POST** `/youtube/formats`

Request:

```json
{
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}
```

Response:

```json
{
  "title": "Video title",
  "formats": [
    {
      "format_id": "18",
      "ext": "mp4",
      "resolution": "360p",
      "filesize": 12345678
    }
  ]
}
```

---

### 🔹 3. Videoni yuklab olish (oqim bilan)

**POST** `/youtube/download/stream`

Request:

```json
{
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "format_id": "18"
}
```

Response: `StreamingResponse` (fayl oqim sifatida yuklanadi).

---

## 📝 Swagger Docs

Swagger hujjatlashuvi shu yerda:

```
http://127.0.0.1:8000/docs
```

---

## 📦 Kerakli Kutubxonalar

`requirements.txt`:

```txt
fastapi
uvicorn
yt-dlp
pydantic
```

---

## 📜 Litsenziya

MIT License bilan tarqatiladi.

---

## 🌍 Open Source

Bu loyiha **to‘liq ochiq kodli (Open Source)**.
Istalgan foydalanuvchi undan foydalanishi, fork qilishi va hissa qo‘shishi mumkin.

👉 Agar loyiha yoqqan bo‘lsa, **⭐️ Star bosishni unutmang!**
Bu kichik harakat loyiha rivojiga katta yordam beradi. 🙌
