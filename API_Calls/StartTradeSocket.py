import time

from twisted.internet import reactor
from API_Calls.API import ws_baseEndpoint, client
from binance.websockets import BinanceSocketManager
from API_Calls.CloseTradeSocket import CloseTradeSocket




def process_message(msg):
    if msg['e'] == 'error':
        #bm.stop_socket(conn_key)
        print(msg['e'])
    print(msg)


def StartTradeSocket():
    bm = BinanceSocketManager(client, user_timeout=60)

    conn_key = bm.start_trade_socket('ETHBTC', process_message)

    bm.start()

    time.sleep(10)

    bm.stop_socket(conn_key)

    reactor.stop()