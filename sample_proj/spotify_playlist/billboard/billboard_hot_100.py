from datetime import datetime
from sample_proj.helpers.api.request_client import get
from bs4 import BeautifulSoup

class BillboardHot100:
    def __init__(self):
        self.default_date = datetime.now().strftime("%Y-%m-%d")
        self.billboard_url = 'https://www.billboard.com/charts/hot-100/'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    def get_billboard_hot_100(self, date=None):
        if date is None:
            date = BillboardHot100().default_date

        headers = {
            'User-Agent': self.user_agent
        }
        billboard_response =  get(f'{self.billboard_url}{date}', headers=headers)

        soup = BeautifulSoup(billboard_response, 'html.parser')
        scraped_titles = soup.find_all('div', class_ ='o-chart-results-list-row-container')
        title_list = [item.find('h3', id='title-of-a-story').getText(strip=True) for item in scraped_titles]
        return title_list



b = BillboardHot100()
b.get_billboard_hot_100()