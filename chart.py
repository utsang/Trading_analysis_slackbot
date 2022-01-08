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

def get jsonF(text):
    api = '8fqEYrALHGQeOseKoYVp6442GRNdcFS3'
    ticker = f'{text}'
    limit = '1000'
    year = '2021'
    month = '07'
    day = '01'
    api_url = f'https://api.polygon.io/v2/reference/news?limit={limit}&order=descending&sort=published_utc&ticker={ticker}&published_utc.gte={year}-{month}-{day}&apiKey={api}'
    data = requests.get(api_url).json()
    return data

def getDfresults(data):
    newsdf = pandas.DataFrame(data['results'])
    return newsdf


l = len(newsdf)

for v, row in newsdf.iterrows():
    val = row['published_utc']
    newsdf.at[v,'published_utc'] = val[0:9]

def getDatesJson(newsdf):
    
    list1 = []
    date_imp = []
    for i in range(int(limit)):
        try:
             date_imp = newsdf['results'][i]['published_utc']
             list1.append(date_imp[0:7]) 
        except:    
            pass
        return list1

def getallUrls(newsdf):
    allurl = []
    for t in range(len(newsdf)):
        allurl.append(newsdf['resuts'][t]['published_url'])
        
    return allurl
    
def getStockprice(text):
    
    df = pandas.read_csv(f'{text}.csv')
    
    return df['Close'][len(df)]

def getStock(text):
    df = pandas.read_csv(f'{text}.csv')

def getBullday(df):
    bulldayindex = []
    df['Boolean'] = df['Open'] < df['Close']
    for row_name, row in df.iterrows():
       
        if row['Boolean'] == True:
              bulldayindex.append(row_name)
                
    return bulldayindex

def getBearday(df):
    beardayindex = []
    df['Boolean'] = df['Open'] < df['Close']
    for row_name, row in df.iterrows():
       
        if row['Boolean'] == False:
              beardayindex.append(row_name)
    return beardayindex
#get dates from the ticker csv
def getProperDates(df):
    val1 = []
    findates = []
    for b in range(len(df)):
        val1.append(df['Date'][b])
        findates.append(val1[0:7])
    return findates 

#gives matchinng dates between the final dates and Json dates and gives out relavent news
def getRelnews(findates,list1):
    finalIndexnews = []
    for d in range(len(list1)):
        if findates[d] == list1[d]:
            finalIndexnews.append(d)
    return finalIndexnews
   
    


# candlestick = go.Candlestick(x=df['Date'],
#                 open=df['Open'],
#                 high=df['High'],
#                 low=df['Low'],
#                 close=df['Close'])

# fig = go.Figure(data=[candlestick])
# fig.layout.xaxis.type = 'category'
# fig.update_layout(title_text='AAPL stock over the last year', template = 'plotly_dark')

# fig.show()

