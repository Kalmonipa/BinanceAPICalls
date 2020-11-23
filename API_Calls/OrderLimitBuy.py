from binance.client import Client
from API_Calls.API import *

# #
# Places an order limit for the price, quantity and symbol specified
# #

def OrderLimitBuy(price, quantity, symbol):
    client = Client(apiKey, apiSecret)

    order = client.order_limit_buy(symbol=symbol, quantity=quantity, price=price)

    jprint(order)

