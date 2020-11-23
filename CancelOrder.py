from binance.client import Client
from API import *

def CancelOrder(symbol, orderId):
    client = Client(apiKey, apiSecret)

    result = client.cancel_order(symbol=symbol, orderId=orderId)

    jprint(result)

