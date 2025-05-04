from sample_proj.stock_prices.api_clients.base_client import BaseClient


class StockClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = 'https://www.alphavantage.co/query'
        self._get_api_key()

    def _get_api_key(self):
        self.data = {
            'path': '/alphavantage_stocks',
            'mount': 'udemy_course'
        }
        self.get_api_key()

    def _get_stock_data(self, ticker):
        params = {
            'symbol' : ticker,
            'apikey' : self.api_key,
            'function' : 'TIME_SERIES_DAILY'
        }
        data = self.get(url=self.url,**params)['Time Series (Daily)']
        data_list = [value for (key, value) in data.items()]
        # print(data_list)
        return data_list

    def _get_two_last_days(self, ticker):
        ticker_data  = self._get_stock_data(ticker=ticker)
        return ticker_data[0]['4. close'], ticker_data[1]['4. close']

    def calculate_percentage_change(self, ticker):
        two_days_data= self._get_two_last_days(ticker=ticker)
        two_days_diff = float(two_days_data[0]) - float(two_days_data[1])
        return round(two_days_diff / float(two_days_data[0]) * 100, 2)



s = StockClient()
change = s.calculate_percentage_change('JNJ')
print(f'change = {change}')

