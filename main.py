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
cmds = {0:"join",1:"leave",2:"web"}

# A decorator function to start
@client.event
async def on_ready():
  print(f"{client.user} has connected to Discord!\nHello World")

# A decorator function to read message the send response
@client.event
async def on_message(message):
  count = 0
  msg = message.content.lower()
  author = message.author
  emoji = ["👀","👋","👉","👈","👍"]

  if author == client.user:
    return

  if msg == pfx:
    gds = [x.name for x in client.guilds]
    await message.reply( "\n".join(gds))
    await message.add_reaction(emoji[1])
    await message.add_reaction(emoji[2])
    await message.add_reaction(emoji[3])

  if msg == (pfx+msg[len(pfx):] not in cmds):
    rpl = f"**I'm currently under-development,{author}"
    await message.reply(rpl+"\n**"+str(count += 1)+"**")

# Actual start logging-in
client.run(TOKEN)
