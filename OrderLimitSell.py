from binance.client import Client
from API import *

def OrderLimitSell(price, quantity, symbol):
    client = Client(apiKey, apiSecret)

    order = client.order_limit_sell(symbol=symbol, quantity=quantity, price=price)

    jprint(order)
