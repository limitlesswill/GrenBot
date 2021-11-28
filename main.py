# importing OS to deal with future files at least ...
import os

# Importing discord library
import discord

# Loading TOKEN from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Instantiate an object of the client
client = discord.Client()

# A decorator function to start
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!\nHello World")

# A decorator function to read message the send response
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("tree "):
        gds = [x.name for x in client.guilds]
        msg = f"I\'m currently under-development , <@{message.author.id}> \n please try again later \n Your message content was \n ```{message.content}```\n"  
        await message.channel.send(msg+"\n".join(gds))

# Actual start logging-in
client.run(TOKEN)
