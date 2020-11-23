from GetOpenOrders import *
from GetTicker import GetTicker


def GetCandles(symbol):
    client = Client(apiKey, apiSecret)

    candles = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_30MINUTE)

    jprint(candles)

    for candle in candles:
        openTime = candle[0]
        open = candle[1]
        high = candle[2]
        low = candle[3]
        close = candle[4]
        volume = candle[5]
        closeTime = candle[6]
        quoteAssetVolume = candle[7]
        numTrades = candle[8]
        takerBuyBase = candle[9]
        takerBuyQuote = candle[10]
        ignore = candle[11]



#    print(openTime)
#    print(open)
#   print(high)
#    print(low)
#    print(close)
#    print(volume)
#    print(closeTime)
#    print(quoteAssetVolume)
#    print(numTrades)
#    print(takerBuyBase)
#    print(takerBuyQuote)
