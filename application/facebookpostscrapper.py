import pandas as pd
from facebook_page_scraper import Facebook_scraper


class FacebookPostsScraper:
    def scrape_data(self, page_name, posts_count=10, proxy_port=10001, browser="firefox", timeout=60, headless=True):

        # Scrap new data for each page
        try:
            proxy = f'IP:{proxy_port}'
            scraper = Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)
            json = scraper.scrap_to_json()
        except:
            print(f"can't scrap this page {page_name}")
        print(json)
        data = pd.read_json(json,orient='index')
        return data


if __name__ == '__main__':
    fbsc = FacebookPostsScraper()
    data = fbsc.scrape_data("Elyadata")
    print(data)
