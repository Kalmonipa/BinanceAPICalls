from binance.client import Client
from API import *

def GetAccInfo():
    client = Client(apiKey, apiSecret)

    accountInfo = client.get_account()

    jprint(accountInfo)

