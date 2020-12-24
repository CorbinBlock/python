import requests
import alphavantage
import csv
import pandas

API_URL = "https://www.alphavantage.co/query"

data = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "GOEV",
    "outputsize": "full",
    "datatype": "csv",
    "apikey": "D46872A04A9M1143LDD",
}

response = requests.get(API_URL, data)
df = pandas.DataFrame(response)
print('DataFrame:', df)
stock_csv_data = df.to_csv('GOEV.csv', index=True)
