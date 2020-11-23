from binance.client import Client
from API import *

def GetTrades(symbol):
    client = Client(apiKey, apiSecret)

    trades = client.get_my_trades(symbol=symbol)

    jprint(trades)

