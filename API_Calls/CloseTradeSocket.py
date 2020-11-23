

# #
# Closes a trade socket
# #

def CloseTradeSocket(conn_key, bm):
    bm.stop_socket(conn_key)


