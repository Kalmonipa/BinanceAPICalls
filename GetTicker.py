from binance.client import Client
from API import *

def GetTicker():
    client = Client(apiKey, apiSecret)

    tickers = client.get_ticker()

    jprint(tickers)