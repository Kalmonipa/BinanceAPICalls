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

        tradeTimeUTC = datetime.fromtimestamp(msg['E'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
        print("Time: {} - Price Chg: {} - Price Chg %: {} - Weighted Avg Price: {} - First Trade Price: {} - Last Price: {} - Best Bid: {} - Best ask: {} - Open Price: {} - High: {} - Low: {} ".format(tradeTimeUTC,
                                                                                                                                                                                                         msg['p'],
                                                                                                                                                                                                         msg['P'],
                                                                                                                                                                                                         msg['w'],
                                                                                                                                                                                                         msg['x'],
                                                                                                                                                                                                         msg['c'],
                                                                                                                                                                                                         msg['b'],
                                                                                                                                                                                                         msg['a'],
                                                                                                                                                                                                         msg['o'],
                                                                                                                                                                                                         msg['h'],
                                                                                                                                                                                                         msg['l']))


# #
# Starts a trade socket to live data for BTCBUSD ticker for 10 seconds
# #
def StartSymbolTickerSocket():
    bm = BinanceSocketManager(client, user_timeout=60)

    conn_key = bm.start_symbol_ticker_socket('BTCBUSD', process_message)

    bm.start()

    time.sleep(10)

    bm.stop_socket(conn_key)

    reactor.stop()