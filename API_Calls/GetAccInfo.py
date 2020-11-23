from binance.client import Client
from API_Calls.API import *

# #
# Gets my account info
# All my balances for all types on Binance
#

def GetAccInfo():
    client = Client(apiKey, apiSecret)

    accountInfo = client.get_account()

    jprint(accountInfo)

