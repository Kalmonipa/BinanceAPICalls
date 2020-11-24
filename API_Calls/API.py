import json
from binance.client import Client

api_baseEndpoint = "https://api.binance.com"
ws_baseEndpoint = "wss://stream.binance.com:9443"

apiKey = ''
apiSecret = ''

client = Client(apiKey, apiSecret)

def jprint(obj):
    text = json.dumps(obj,sort_keys=True, indent=4)
    print(text)


