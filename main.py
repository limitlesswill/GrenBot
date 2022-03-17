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
cmds = ["join","leave","web","init"]

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

  ### redirect system output through the bot

  if cmd and (msg.split()[0][len(pfx):] == cmds[3]):
    initcmd = msg[len(pfx)+len(cmds[3])+1:]
    await message.reply(f"initializing {initcmd} ...\nLength: {len(initcmd)}")
    one = ""
    t = os.popen(initcmd,stdout=one)
    tr = repr(t.read())
    await message.reply(f"length of the pipeline: {len(tr)}")
    await message.reply(f"{tr} one:{one}")
    t.close()
    return
    
  if msg == pfx:
    gds = [x.name for x in client.guilds]
    await message.reply( "\n".join(gds))
    await message.add_reaction(emoji[1])
    await message.add_reaction(emoji[2])
    await message.add_reaction(emoji[3])
    return

  if cmd and (msg.split()[0][len(pfx):] not in cmds):
    txt = msg[len(pfx):].lstrip().replace(" ","+")
    link = f"https://translate.google.com.vn/translate_tts?ie=UTF-8&q={txt}&tl=en&client=tw-ob"
    embed=discord.Embed(title=f"**{msg[len(pfx):].lstrip().upper()}**", url=link, description="", color=0x00ff00)
    embed.set_thumbnail(url=client.user.display_avatar)
    embed.set_footer(text=f"{message.author}",icon_url=f"{message.author.display_avatar}")
    await message.reply(embed=embed)

    rpl = f"**I'm currently under-development**,{author}"
    global count
    count += 1
    await message.reply(rpl+f"\ncount **{str(count)}**")
    return

  if cmd and (msg.split()[0][len(pfx):] == cmds[2]):
    ## needs caution , carefully handles the text here
    try:
      url = msg[len(pfx)+len(cmds[2])+1:]
      obj = hweb(url)
      await message.reply(f"{url}\ninitializing hweb object\n1. **{obj.result}**")
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
