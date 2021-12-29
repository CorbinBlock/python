import requests
import alphavantage
import csv
# import pandas
import json
import os

# API key stored in environment variable

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
API_URL = "https://www.alphavantage.co/query"

data = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "PLTR",
    "outputsize": "full",
    "datatype": "json",
    "apikey": api_key,
}

response = requests.get(API_URL, data)

response.json()

# parse JSON string into python dict
json_data = json.loads(response.text)
print(type(json_data))
print(json_data["Time Series (Daily)"])

with open("data_file.json", "w") as write_file:
    json.dump(json_data, write_file)

# df = pandas.DataFrame(response)
# print('DataFrame:', df)
#
#
# stock_csv_data = df.to_csv('GOEV.csv', index=True)
