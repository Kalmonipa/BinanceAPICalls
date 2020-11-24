import requests
import discord
from discord import Webhook, RequestsWebhookAdapter

def postDiscord(text):
    webhook = Webhook.partial('', '', adapter=RequestsWebhookAdapter())

    webhook.send(text)



