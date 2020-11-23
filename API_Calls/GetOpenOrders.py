from binance.client import Client
from API_Calls.API import *

# #
# Gets my open orders for the specified symbol
# #

def GetOpenOrders(symbol):
    client = Client(apiKey, apiSecret)

    orders = client.get_open_order(symbol=symbol)

    jprint(orders)


