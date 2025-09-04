from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_formats_endpoint():
    response = client.post("/youtube/formats", json={"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"})
    # API hech bo‘lmasa JSON qaytarishini tekshiramiz
    assert response.status_code == 200
    assert "title" in response.json()
