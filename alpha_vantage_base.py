import requests
import json
from datetime import date, timedelta
from config import Config


class AlphaVantageBase:

    def execute(self, companies):
        api_key = Config.alpha_vantage_api_key

        yesterday = date.today() - timedelta(2)
        datapoint = yesterday.strftime('%Y-%m-%d')

        for company in companies:
            datafeed_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+company+'&apikey='+api_key
            datafeed = requests.get(datafeed_url)
            company_data = json.loads(datafeed.content)
            time_series = company_data.get('Time Series (Daily)').get(datapoint)
            latest_close_price = time_series.get('4. close')
            print(company + ': ' + latest_close_price)
            print('--- ---')