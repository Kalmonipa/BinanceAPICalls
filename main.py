from GetAccInfo import GetAccInfo
from GetBalance import GetBalance
from GetTicker import GetTicker
from GetAllOrders import GetAllOrders
from GetOpenOrders import GetOpenOrders
from GetTrades import GetTrades
from OrderLimitBuy import OrderLimitBuy
from OrderLimitSell import OrderLimitSell
from CancelOrder import CancelOrder
from GetCandles import GetCandles
from discordWebhook import postDiscord

if __name__ == '__main__':

    GetCandles('BTCBUSD')
    #GetAccInfo()
    #GetBalance('BTC')
    #GetTicker()
    #GetOrderBook()
    #GetOpenOrders()
    #GetTrades('day')
    #postDiscord('hi there')

