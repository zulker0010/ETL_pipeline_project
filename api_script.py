import requests 
import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine, text

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

#test code to see if dataframe can be ported to a csv file from json
df.to_csv('df.csv', sep=',', index=False, na_rep='Nan', header=True, compression='infer', date_format='dd/mm/yyyy', decimal='.')

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:13112001@localhost/kidstime_bd')
df.to_sql(name='Transactions', con=engine, index=False, if_exists='replace')

#show data from Transactions table 
with engine.connect() as connection:
 result = connection.execute(text('SELECT * FROM public."Transactions"'))
 for row in result:
  print(row)
