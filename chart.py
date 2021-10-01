#TO Do check list now
#Global variable for the ticker name so it can be accesed, play around more with plotly and matlib try and get volume data, rsi and macd for momentum analysis as well

import plotly.graph_objects as go
import pandas 
from datetime import datetime
import requests
import csv
import json
from io import StringIO
import slack
import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.')/ '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel='#tradingtest', text = input('Enter your Message here: '))

api = '8fqEYrALHGQeOseKoYVp6442GRNdcFS3'
ticker = 'AAPL'
limit = '1000'
year = '2021'
month = '04'
day = '05'
api_url = f'https://api.polygon.io/v2/reference/news?limit={limit}&order=descending&sort=published_utc&ticker={ticker}&published_utc.gte={year}-{month}-{day}&apiKey={api}'
data = requests.get(api_url).json()
#date = (data['results'][0]['published_utc'])


#first_nine = date[0:9]
#print(first_nine)

newsdf = pandas.DataFrame(data['results'])
#print(newsdf)

#print(newsdf['published_utc'])
l = len(newsdf)

for v, row in newsdf.iterrows():
    val = row['published_utc']
    newsdf.at[v,'published_utc'] = val[0:9]




list1 = []
date_imp = []

for i in range(int(limit)):
    try:
         date_imp = data['results'][i]['published_utc']
         list1.append(date_imp[0:9]) 
    except:    
        pass



#print(list1)
print(date_imp)
#df = pandas.read_csv(StringIO('yahoo.csv'), sep = " ")
df = pandas.read_csv('yahoo.csv')

#print(df)

df['Boolean'] = df['Open'] < df['Close']


# secList = []

# for row_name, row in df.iterrows():
    
#     if row['Boolean'] == False:
        
#         if list1[row_name] ==  row['Date']:
#             print(row_name, 'Boolean is false')
#             secList.append([row_name])
#         else:
#            print('No matching date found') 
           

#     else:
#         print('Boolean is true: ', row_name)




# candlestick = go.Candlestick(x=df['Date'],
#                 open=df['Open'],
#                 high=df['High'],
#                 low=df['Low'],
#                 close=df['Close'])

# fig = go.Figure(data=[candlestick])
# fig.layout.xaxis.type = 'category'
# fig.update_layout(title_text='AAPL stock over the last year', template = 'plotly_dark')

# fig.show()

