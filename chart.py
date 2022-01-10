import yfinance as yf
import pandas
import requests
import csv
import json
from io import StringIO
#import slack
from datetime import date


def getjsonF(text):
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


def getDatesJson(newsdf):
    
    list1 = []
    date_imp = []
    for i in range(len(newsdf)):
             date_imp = newsdf['published_utc'][i]
             list1.append(date_imp[0:7]) 
    
    return list1

def getallUrls(newsdf):
    allurl = []
    for t in range(len(newsdf)):
        allurl.append(newsdf['article_url'][t])
        
    return allurl

def do_something(text):

      d4 = date.today()
      tickerWant = text
      data = yf.download(tickerWant, start="2021-09-5", end=d4)
      data.to_csv(rf'C:\workfin\demofin\\{tickerWant}.csv') 
    
def getStockprice(text):
    
    df = pandas.read_csv(f'C:\workfin\demofin\{text}.csv')
    
    return df['Close'][len(df)-1]


def getStock(text):
    df = pandas.read_csv(f'C:\workfin\demofin\{text}.csv')
    return df

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
        val1 = df['Date'][b]
        findates.append(val1[0:7])
    
    return findates 

#gives matchinng dates between the final 
## dates and Json dates and gives out relavent news

def getRelnews(findates,list1):
    finalIndexnews = []
    for d in range(0,len(findates)-1):
        if findates[d] == list1[d]:
            finalIndexnews.append(d)
    
    return finalIndexnews
   
def getBulldates(bulldayindex,findates):
##This function just appends the bull day indexes found and finds them on findates which has all the dates, so 
##from the csv file this function just gets the bull days
    bulldayDates = []
    for gg in range(len(bulldayindex)):
        bulldayDates.append(findates[bulldayindex[gg]])
    return bulldayDates

def getBearDates(beardayindex,findates):
    beardayDates = []
    for ggf in range(len(beardayindex)):
        beardayDates.append(findates[beardayindex[ggf]])
    return beardayDates
def bullDayurl(bulldayDates,list1,allurl):
    bullUrl = []
    for t in range(len(bulldayDates)):
        if bulldayDates[t] == list1[t]:
            bullUrl.append(allurl[t])
        return bullUrl
def bearDayurl(beardayDates,list1,allurl):
    bearUrl = []
    for tt in range(len(beardayDates)):
        if beardayDates[tt] == list1[tt]:
            bearUrl.append(allurl[tt])
        return bearUrl

def do_something(text):

      d4 = date.today()
      tickerWant = text
      data = yf.download(tickerWant, start="2021-09-5", end=d4)
      data.to_csv(rf'C:\workfin\demofin\\{tickerWant}.csv') 



      ##CHECK STUFF##
      t = getjsonF('AAPL') #return data
# g = getDfresults(t) #pass in data, returns newsdf
# f = getDatesJson(g) #pass in newsdf, returns list1 dates
# hh = getallUrls(g) #retunrs list of all urls, pass in newsdf
# stockm = do_something('AAPL') #doesn't return anything,
## just outputs the .csv file
# priceS = getStockprice('AAPL')
# jusStock = getStock('AAPL') #takes in text,returns df
# bullkoin = getBullday(jusStock) #takes in df, returns index of bullday
# bearkodin = getBearday(jusStock) #takes in df, returns index of bear days
# fulldates = getProperDates(jusStock) #takes in df, returns 
# findates which is all dates formatted
# finNews = getRelnews(fulldates,f) #takes in fulldates(dates fofrmatted from csv) and list1, dates from Json file, returns finalindexes for the all urls(example u can use the returned value from this to get the appropiate urls, so example in this u can do hh[finnews[5]])
# bulldin = getBulldates(bullkoin,fulldates)
# beardin = getBearDates(bearkodin,fulldates) #both of them take their respective indexes for bull/bear days and returns the date where they matched(rom the csv file this function just gets the bull days)
# puraiBull = bullDayurl(bulldin,f,hh)
# puraiBear = bearDayurl(beardin,f,hh)
