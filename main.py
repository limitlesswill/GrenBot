import os

# Importing discord and dotenv libraries
import discord
from dotenv import load_dotenv

# Loading TOKEN from bot.env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Instantiate an object of the client
client = discord.Client()

# A decorator function to start
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!\nHello World")

# Actual start logging-in
client.run(TOKEN)
