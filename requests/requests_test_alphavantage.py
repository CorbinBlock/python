import json
import os
import requests

api_key = ''

base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'TIME_SERIES_DAILY_ADJUSTED',
                 'symbol': 'IBM',
                         'apikey': api_key}

response = requests.get(base_url, params=params)
print(response.content)
