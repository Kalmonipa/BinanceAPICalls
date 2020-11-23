from binance.client import Client
from API_Calls.API import *

# #
# Places an order limit to sell at the price, quantity and symbol specified
# #

def OrderLimitSell(price, quantity, symbol):
    client = Client(apiKey, apiSecret)

    order = client.order_limit_sell(symbol=symbol, quantity=quantity, price=price)

    jprint(order)
