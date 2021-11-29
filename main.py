# importing OS to deal with future files at least ...
import os

# Importing discord library
import discord

# Loading TOKEN from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Instantiate an object of the client
client = discord.Client()

# Prefix of the bot
pfx = "."

# A decorator function to start
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!\nHello World")

# A decorator function to read message the send response
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower()
    if msg.startswith(pfx) and len(msg) > 1 :
        rpl = f"I\'m currently under-development , {message.author} \n please try again later \n Your message content was \n ```{message.content}```\n"  
        await message.reply(rpl+f" \nVoice: {message.author.voice}")
        emoji = ["👋","👍"]
        await message.add_reaction(emoji[0])
        await message.add_reaction(emoji[1])

    if msg == pfx:
        gds = [x.name for x in client.guilds]
        await message.reply( "\n".join(gds), mention_author=False )
        emoji = ["👋","👉","👈"]
        await message.add_reaction(emoji[0])
        await message.add_reaction(emoji[1])
        await message.add_reaction(emoji[2])
     

# Actual start logging-in
client.run(TOKEN)
