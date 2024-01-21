from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_scrape_facebook_data():
    response = client.post("/api/scrape_posts", json={"page_name": "Elyadata"})
    assert response.status_code == 200
    assert "scraped_data" in response.json()
