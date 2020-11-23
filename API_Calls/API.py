import json
from binance.client import Client

api_baseEndpoint = "https://api.binance.com"
ws_baseEndpoint = "wss://stream.binance.com:9443"

apiKey = 'AFATuuae51yUecDfRA2nZkYy5dlTNgXycucoWAYtpzXW0v1Gl3hUlhCu8mQO9eJN'
apiSecret = 'HlgPZOxRAD6yaCHhSE3m5LRkR3XFYpxN4MUiYFtkSsuLe6X8irMo3dJobvajWjsl'

client = Client(apiKey, apiSecret)

def jprint(obj):
    text = json.dumps(obj,sort_keys=True, indent=4)
    print(text)


