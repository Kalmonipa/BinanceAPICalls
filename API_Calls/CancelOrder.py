from binance.client import Client
from API_Calls.API import *

# #
# Cancels the order that we specify
# #

def CancelOrder(symbol, orderId):
    client = Client(apiKey, apiSecret)

    result = client.cancel_order(symbol=symbol, orderId=orderId)

    jprint(result)

