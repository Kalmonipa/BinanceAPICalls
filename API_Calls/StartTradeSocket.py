import time
from _datetime import datetime

from twisted.internet import reactor
from API_Calls.API import ws_baseEndpoint, client
from binance.websockets import BinanceSocketManager
from API_Calls.CloseTradeSocket import CloseTradeSocket




def process_message(msg):
    if msg['e'] == 'error':
        #bm.stop_socket(conn_key)
        print(msg['e'])
    else :

        tradeTimeUTC = datetime.fromtimestamp(msg['T'] / 1000).strftime('%Y-%m-%d %H:%M:%S')

        if msg['m'] == True :
            tradeType = 'Sell'
        else :
            tradeType = 'Buy'

        print("Time: {} - Trade Type: {} - Price: {} - Quantity: {}".format(tradeTimeUTC,
                                                                  tradeType,
                                                                  msg['p'],
                                                                  msg['q']))


# #
# Starts a trade socket to live data for BTCBUSD ticker for 10 seconds
# #
def StartTradeSocket():
    bm = BinanceSocketManager(client, user_timeout=60)

    conn_key = bm.start_trade_socket('BTCBUSD', process_message)

    bm.start()

    time.sleep(10)

    bm.stop_socket(conn_key)

    reactor.stop()