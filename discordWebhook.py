import requests
import discord

from discord import Webhook, RequestsWebhookAdapter

def postDiscord(text):
    webhook = Webhook.partial('780039524305600533', 'VPwRq9pRucvxz-B-KWL0nkBj2jIIkcjrP_dA51LIKQPGwb_WsKdGMEOucam8ys2krJuS', adapter=RequestsWebhookAdapter())

    webhook.send(text)



