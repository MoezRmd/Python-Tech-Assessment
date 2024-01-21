from fastapi import APIRouter
from application.facebookpostscrapper import FacebookPostsScraper

router = APIRouter()
facebook_scraper = FacebookPostsScraper()

@router.get("/scrape_posts/")  # Changed to POST
async def scrape_facebook_posts(request: dict):
    page_name = request.get("page_name")
    data = facebook_scraper.scrape_data(page_name)
    return {"scraped_data": data}
