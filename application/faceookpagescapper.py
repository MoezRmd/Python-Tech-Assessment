import requests
from bs4 import BeautifulSoup
from facebook_page_scraper import Facebook_scraper


class FacebookScraper:
    def extract_page_description(self, soup):
        desc_element = soup.find("meta", property="og:description")
        if desc_element:
            description = desc_element["content"]
            return description
        return "Description not found"

    def extract_profile_picture(self, soup):
        image_element = soup.find("meta", property="og:image")
        if image_element:
            profile_picture_url = image_element["content"]
            return profile_picture_url
        return "Profile picture not found"

    def scrape_facebook_page(self, page_name, posts_count=10):
        try:
            # Set the parameters for scraping
            page_name = page_name
            browser = "firefox"
            timeout = 60  # 600 seconds
            headless = True

            # Instantiate the Facebook_scraper class
            scrapper = Facebook_scraper(page_name, posts_count, browser, timeout=timeout, headless=headless)

            # Scrape the data
            json_data = scrapper.scrap_to_json()
            # Return the scraped data
            return json_data
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}

    def scrape_data(self, page_url,page_name, posts_count=10):
        try:
            # Scrape data from the provided URL
            response = requests.get(page_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                page_title = soup.title.string if soup.title else "Title not found"
                page_description = self.extract_page_description(soup)
                profile_picture = self.extract_profile_picture(soup)

                # Call the scrape_facebook_page function to get additional data
                facebook_page_data = self.scrape_facebook_page(page_name, posts_count)

                # Combine the data
                combined_data = {
                    "page_title": page_title,
                    "page_description": page_description,
                    "profile_picture": profile_picture,
                    "posts_data": facebook_page_data
                }

                # Save the scraped data to the database
                # self.save_to_database(combined_data)

                # Return the combined data
                return combined_data
            else:
                return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}
