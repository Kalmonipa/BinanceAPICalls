from binance.client import Client
from API_Calls.API import *

# #
# Gets my balance of the specified asset
# #

def GetBalance(asset):
    client = Client(apiKey, apiSecret)

    balance = client.get_asset_balance(asset=asset)

    jprint(balance)

