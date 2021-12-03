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
  if message.author == client.user:
    return

  await message.reply(f"here we go \n{message.guild}")
  dmsg = f"**Invite me to a server so we can play\nhttps://discordapp.com/oauth2/authorize?client_id=569724616210382875&scope=bot&permissions=277129284672**"
  await message.reply(dmsg)
  await message.reply(f"message.author.avatar_url\n{message.author.avatar_url}")

  msg = message.content.lower()
  cmd = msg.startswith(pfx)
  author = message.author
  emoji = ["👀","👋","👉","👈","👍"]

  if msg == pfx:
    gds = [x.name for x in client.guilds]
    await message.reply( "\n".join(gds))
    await message.add_reaction(emoji[1])
    await message.add_reaction(emoji[2])
    await message.add_reaction(emoji[3])

  if cmd and (msg[len(pfx):] not in cmds):
    rpl = f"**I'm currently under-development**,{author}"
    global count
    count += 1
    await message.reply(rpl+f"\ncount **{str(count)}**")

  if cmd and (msg[len(pfx):] == cmds[2]):
    try:
      obj = hweb()
      txt = obj.get_data()
      await message.reply(txt)
    except:
      await message.reply("exception")
    await message.reply("web command issued")
    

# Actual start logging-in
client.run(TOKEN)
