from binance.client import Client
from API import *

def GetBalance(asset):
    client = Client(apiKey, apiSecret)

    balance = client.get_asset_balance(asset=asset)

    jprint(balance)

