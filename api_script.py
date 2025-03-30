import requests 
import pandas as pd
import sqlite3

url = 'https://data-api.coindesk.com/index/cc/v1/latest/tick?market=cadli&instruments=BTC-USD,ETH-USD&apply_mapping=true'

header = {
 "Postman-Token": "<calculated when request is sent>",
 "Host":"calculated when request is sent",
 "User-Agent": "PostnmanRuntime/7.40.0",
 "Accept": "*/*",
 "Accept-Encoding": "deflate",
 "Connection": "keep-alive"
}

response = requests.get(url, headers=header)
print(response)
response_data = response.json()
print(response_data)