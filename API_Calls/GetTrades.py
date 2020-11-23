from binance.client import Client
from API_Calls.API import *

# #
# Gets all my trade history for the specified symbol
# BTCBUSD is the one we care about
# #

def GetTrades(symbol):
    client = Client(apiKey, apiSecret)

    trades = client.get_my_trades(symbol=symbol)

    jprint(trades)

