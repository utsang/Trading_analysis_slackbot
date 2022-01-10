import os
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request
from pathlib import Path 
from dotenv import load_dotenv
import shutil
from demofin import getjsonF, getDfresults, getDatesJson, getallUrls, getStockprice,getStock, getBullday, getBearday,getProperDates,getRelnews,getBulldates,getBearDates,bullDayurl,bearDayurl,do_something
## t = getjsonF('AAPL') #return data
## g = getDfresults(t) #pass in data, returns newsdf
## f = getDatesJson(g) #pass in newsdf, returns list1 dates
## hh = getallUrls(g) #retunrs list of all urls, pass in newsdf
## stockm = do_something('AAPL') #doesn't return anything,
# # just outputs the .csv file
## priceS = getStockprice('AAPL')
## jusStock = getStock('AAPL') #takes in text,returns df
## bullkoin = getBullday(jusStock) #takes in df, returns index of bullday
## bearkodin = getBearday(jusStock) #takes in df, returns index of bear days
## fulldates = getProperDates(jusStock) #takes in df, returns 
# #findates which is all dates formatted
## finNews = getRelnews(fulldates,f) #takes in fulldates(dates
# # formatted from csv) and list1,
# # dates from Json file, returns 
# #finalindexes for the all urls
# #(example u can use the returned value
# # from this to get the appropiate urls, 
# #so example in this u can do hh[finnews[5]])

## bulldin = getBulldates(bullkoin,fulldates)
## beardin = getBearDates(bearkodin,fulldates) #both of them take their respective indexes for bull/bear days and returns the date where they matched(rom the csv file this function just gets the bull days)
##puraiBull = bullDayurl(bulldin,f,hh)
## puraiBear = bearDayurl(beardin,f,hh) #tries retrieving the articles and stores in individual 

env_path = Path('.')/'.env'

load_dotenv(dotenv_path=env_path)





app = App(token=os.environ.get('SLACK_TOKEN'), signing_secret=os.environ.get('SIGNING_SECRET'))


flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

@app.event('message')
def print_message(event,say):
  msg_txt = event['text']
  do_something(msg_txt)
  
  t = getjsonF(msg_txt) #return data
  g = getDfresults(t) #pass in data, returns newsdf
  f = getDatesJson(g) #pass in newsdf, returns list1 dates
  hh = getallUrls(g) #retunrs list of all urls, pass in newsdf
  jusStock = getStock(msg_txt)
  fulldates = getProperDates(jusStock)
  indexNews = getRelnews(fulldates,f)
  priceS = getStockprice(msg_txt)
  say(text=f'The price of the Stock currently is ${priceS}')
  newsstuff = hh[indexNews[0]]
  say(f'Relavant news article: {newsstuff}')
  os.remove(f"{msg_txt}.csv")


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
  return handler.handle(request)


if __name__ == "__main__":
  app.start(3000)  # POST http://localhost:3000/slack/events
