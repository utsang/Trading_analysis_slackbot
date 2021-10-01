import yfinance as yf
import pandas as pd

tickerWant = input ('Enter the ticker you want ')

ticker_chk = yf.Ticker(tickerWant)

history = ticker_chk.history(period="ytd")

print(history.to_csv())

history.to_csv(rf'C:\work\demo\data\{tickerWant}.csv')
