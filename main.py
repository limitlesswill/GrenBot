from os import getenv
from base import client
from message import on_message
from cornjob import on_ready,test


# Loading TOKEN from environment variables
TOKEN = getenv('DISCORD_TOKEN')


client.run(TOKEN)
