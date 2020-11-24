from API_Calls.PingServer import PingServer
import time

# #
# Calls the PingServer function every 60 seconds
# #

def checkConnectionToServer():

    start = time.time()
    time.clock()

    elapsedTime = 0

    while elapsedTime < 61 :
        elapsedTime = time.time() - start
        time.sleep(1)
        if elapsedTime > 59 :
            PingServer()
            start = time.time()