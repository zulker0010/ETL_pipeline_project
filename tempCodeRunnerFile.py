import requests 
import pandas as pd
import sqlite3

url = 'https://data-api.coindesk.com/index/cc/v1/historical/days?market=cadli&instrument=BTC-USD&limit=1000&aggregate=1&fill=true&apply_mapping=true&response_format=JSON'

header = {
'Content-type': 'application/json ; charset = UTF-8'
}

response = requests.get(url,headers=header)
print(response)
response_data = response.json()
print(response_data)

df = pd.json_normalize(response_data, 'Data')
print(df)