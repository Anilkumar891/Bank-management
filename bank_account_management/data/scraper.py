# import requests

# class Scraper:
#     def scrape_data(self, url):
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             raise Exception("Failed to retrieve data from the web interface.")
import requests

class Scraper:
    def scrape_data(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.reason}")
            raise Exception("Failed to retrieve data from the web interface.")
