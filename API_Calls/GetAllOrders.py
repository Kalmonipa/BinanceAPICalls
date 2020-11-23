from binance.client import Client
from API_Calls.API import *

# #
# Gets my current orders
# #
def GetAllOrders(symbol,limit):
    client = Client(apiKey, apiSecret)

    orders = client.get_all_orders(symbol=symbol, limit=limit)

    jprint(orders)

