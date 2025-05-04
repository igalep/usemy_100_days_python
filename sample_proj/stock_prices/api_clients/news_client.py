import pprint

from sample_proj.stock_prices.api_clients.base_client import BaseClient

class NewsClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = 'https://newsapi.org/v2/everything'
        self._get_api_key()


    def _get_api_key(self):
        self.data = {
            'path': '/news_api',
            'mount': 'udemy_course'
        }
        self.get_api_key()


    def get_news(self):
        params = {
            'q' : 'jnj stock',
            'apiKey' : self.api_key,
            'searchIn': 'title,content',
        }

        news = self.get(url=self.url, **params)['articles'][:3]
        pprint.pprint(news)



nc = NewsClient()
nc.get_news()