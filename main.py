# importing OS to deal with future files at least ...
import os
from sweb import hweb
# Importing discord library
import discord

# Loading TOKEN from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Instantiate an object of the client
client = discord.Client()

# Prefix of the bot
count = 0
pfx = "."
cmds = ["join","leave","web"]

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
    await message.reply( "\n".join(gds))
    await message.add_reaction(emoji[1])
    await message.add_reaction(emoji[2])
    await message.add_reaction(emoji[3])

  if msg[len(pfx):] not in cmds and len(pfx) > 1:
    rpl = f"**I'm currently under-development**,{author}"
    global count
    count += 1
    await message.reply(rpl+f"\ncount **{str(count)}**")

  if msg[len(pfx):] == cmds[3]:
    try:
      obj = hweb()
      txt = obj.get_data()
      await message.reply(txt)
    except:
      await message.reply("exception")
    await message.reply("web command issued")
    

# Actual start logging-in
client.run(TOKEN)
