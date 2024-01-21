from fastapi import APIRouter
from application.facebookpostscrapper import FacebookPostsScraper

router = APIRouter()
facebook_scraper = FacebookPostsScraper()

@router.get("/scrape_posts/{page_name}")  # Changed to POST
async def scrape_facebook_posts(page_name: str):
    data = facebook_scraper.scrape_data(page_name)
    return {"scraped_data": data}
@router.get("/")
def read_root():
    return {"message": "Hello!"}