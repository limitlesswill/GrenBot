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
  if (message.author == client.user) or (message.author.bot):
    return

  if message.guild is None:
    embed=discord.Embed(title="Invite me to your **server**", url="https://discordapp.com/oauth2/authorize?client_id=569724616210382875&scope=bot&permissions=277129284672", description="", color=0x00ff00)
    embed.set_author(name=f"{message.author}", url="https://discordapp.com/oauth2/authorize?client_id=569724616210382875&scope=bot&permissions=277129284672", icon_url=f"{message.author.display_avatar}")
    embed.set_thumbnail(url=client.user.display_avatar)
    embed.set_footer(text=f"I'm a nice bot under construction")
    await message.reply(embed=embed)
    return

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
    here = msg[len(pfx):]
    li = f"https://translate.google.com.vn/translate_tts?ie=UTF-8&q={here.replace(" ","+")}&tl=en&client=tw-ob"
    rpl = f"[here]({li})\n**I'm currently under-development**,{author}"
    global count
    count += 1
    await message.reply(rpl+f"\ncount **{str(count)}**")

  if cmd and (msg[len(pfx):] == cmds[2]):
    try:
      obj = hweb()
      await message.reply(f"initializing hweb object\n1. **{obj.result}**")
      txt = obj.get_data()
      MX = 1000
      await message.reply(f"len(get_data()): **{len(txt)}**\nLast working stage: **{obj.result}**")
      while len(txt) >= MX:
        tmp = txt[:MX]
        await message.reply(f"``` {tmp} ```")
        txt = txt[MX:]
      await message.reply(f"``` {txt} ```")
    except Exception as ex:
      await message.reply(f"exception: **{type(ex).__name__}**\n{str(ex)}\n2. Last working stage: **{obj.result}**")
    await message.reply("web command issued")
    

# Actual start logging-in
client.run(TOKEN)
