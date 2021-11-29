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
    msg = message.content.lower()
    author = message.author
    emoji = ["👀","👋","👉","👈","👍"]

    if author == client.user:
        return

    if msg == pfx:
        gds = [x.name for x in client.guilds]
        await message.reply( "\n".join(gds), mention_author=False )
        await message.add_reaction(emoji[1])
        await message.add_reaction(emoji[2])
        await message.add_reaction(emoji[3])

    elif msg == pfx+pfx:
        if message.guild.voice_client is None:
           await message.channel.reply("I'm not even in a voice channel")
           return
        else:
           await message.guild.voice_client.disconnect()
           await message.add_reaction(emoji[1])
           await message.reply("See you later")

    elif msg.startswith(pfx) and len(msg) > 1 :
        rpl = f"I\'m currently under-development , {author} \n please try again later \n Your message content was \n ```{message.content}```\n"  
        await message.reply(rpl)
        await message.add_reaction(emoji[1])
        if author.voice is None:
           await message.reply("You are not in a **Voice Channel**")
           return
        else:
           if author.voice.channel.id != message.voice_client.channel.id:
              message.guild.voice_client.move_to(message.author.voice.channel)
           else:
              await author.voice.channel.connect()
              await message.add_reaction(emoji[4])
              await message.add_reaction(emoji[1])
              await message.reply("**I'm Connecting...**",mention_author=False)
     

# Actual start logging-in
client.run(TOKEN)
