from binance.client import Client
from API import *

def GetOpenOrders(symbol):
    client = Client(apiKey, apiSecret)

    orders = client.get_open_order(symbol=symbol)

    jprint(orders)


