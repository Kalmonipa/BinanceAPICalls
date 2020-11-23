from API_Calls.StartTradeSocket import StartTradeSocket
from ServerConnectionCheck import checkConnectionToServer

if __name__ == '__main__':

    # Need to uncomment this for the final product so it will check the connection to the server
    #checkConnectionToServer()

    StartTradeSocket()

    #GetCandles("BTCBUSD")
    #PingServer()

