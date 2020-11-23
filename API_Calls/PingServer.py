from API_Calls.API import client
from discordWebhook import postDiscord

# #
# Checks the system status of the server every 60 seconds
# If it gets a non-normal response it will post to discord
# #

def PingServer():

    response = client.get_system_status()

    if response["msg"] != "normal" or response["status"] != 0 :
        postDiscord("System status is getting a {} response from the Binance server".format(response["msg"]))

