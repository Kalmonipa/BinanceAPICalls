from binance.client import Client
from API import *

def OrderLimitBuy(price, quantity, symbol):
    client = Client(apiKey, apiSecret)

    order = client.order_limit_buy(symbol=symbol, quantity=quantity, price=price)

    jprint(order)

