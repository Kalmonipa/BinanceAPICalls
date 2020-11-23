from binance.client import Client
from API_Calls.API import *

# #
# Gets information on all the tickers available
# #

def GetTicker():
    client = Client(apiKey, apiSecret)

    tickers = client.get_ticker()

    jprint(tickers)