from API_Calls.API import *
from datetime import datetime
from binance.client import Client
from discordWebhook import postDiscord

# #
# Gets the candle information for the specified symbol
# Can add in historical data by passing a date as a string in - "1 Dec, 2017"
# #

def GetHistoricalCandles(symbol, timePeriod):
    client = Client(apiKey, apiSecret)

    candles = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_30MINUTE, timePeriod)

    for candle in candles:
        openTime = candle[0]
        openTimeUTC = datetime.utcfromtimestamp(openTime/1000).strftime('%Y-%m-%d %H:%M:%S')
        open = candle[1]
        high = candle[2]
        low = candle[3]
        close = candle[4]
        volume = candle[5]
        closeTime = candle[6]
        closeTimeUTC = datetime.utcfromtimestamp(closeTime / 1000).strftime('%Y-%m-%d %H:%M:%S')
        quoteAssetVolume = candle[7]
        numTrades = candle[8]
        takerBuyBase = candle[9]
        takerBuyQuote = candle[10]
        ignore = candle[11]

