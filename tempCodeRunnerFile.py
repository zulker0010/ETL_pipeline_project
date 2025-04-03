import requests 
import pandas as pd
import psycopg2
from sqlalchemy import create_engine 

url = 'https://data-api.coindesk.com/index/cc/v1/historical/days?market=cadli&instrument=BTC-USD&limit=1000&aggregate=1&fill=true&apply_mapping=true&response_format=JSON'

header = {
'Content-type': 'application/json ; charset = UTF-8'
}

response = requests.get(url,headers=header)
print(response)
response_data = response.json()
print(response_data)

df = pd.json_normalize(response_data, 'Data')
#print(df)

engine = create_engine('postgresql+psycopg2://postgres:13112001@localhost/kidstime_bd')
df.to_sql(name='Payments', con=engine, index=True, if_exists='fail')
