from os import getenv , path
import datetime
from discord.ext import tasks
import savefile as sf
import discord

# Loading TOKEN from environment variables
TOKEN = getenv('DISCORD_TOKEN')

intent = discord.Intents(messages=True, guilds=True)
intent.reactions = True
intent.message_content = True
intent.typing = False
intent.presences = False

# Instantiate an object of the client
client = discord.Client(intents=intent)

# Prefix of the bot
pfx = "."
cmds = ["save","load","peek","send","recent","timestop","timerestart"]

@tasks.loop(minutes=1)
async def test():
    channel = client.get_channel(971240750731890738)
    cur = datetime.datetime.utcnow().strftime("%Y/%D/%w\💚  %I:%M  %p  \💚")
    await channel.send(f"\t\t\t\t\t**{cur}**",delete_after=59)


# A decorator function to start
@client.event
async def on_ready():
  print(f"{client.user} has connected to Discord!\nHello World")
  test.start()

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
  debug = (str(author) == "User#3231")
  emoji = ["👀","👋","👉","👈","👍","💚"]
    
  if debug and (msg == pfx):
    gds = [x.name for x in client.guilds]
    await message.reply( "\n".join(gds),delete_after=sf.settings["deltime"])
    await message.add_reaction(emoji[1])
    await message.add_reaction(emoji[2])
    await message.add_reaction(emoji[3])
    return
  if debug and (msg == (pfx+cmds[0]) ):
    sf.save()
    await message.reply("**Saved**",delete_after=sf.settings["deltime"])
    return
  if debug and (msg == (pfx+cmds[1]) ):
    sf.load()
    await message.reply("**Loaded**",delete_after=sf.settings["deltime"])
    return
  if debug and (msg == (pfx+cmds[2])):
    await message.channel.send(f"file name: {sf.file_name}",delete_after=sf.settings["deltime"])
    await message.channel.send(f"Does it exist: {path.isfile(sf.file_name)}",delete_after=sf.settings["deltime"])
    await message.reply(f"**Data**: {sf.peek()}",delete_after=sf.settings["deltime"])
    await message.reply("**Peek**",delete_after=sf.settings["deltime"])
    return
  if debug and (msg.split()[0] == (pfx+cmds[4]) ):
    # channel format would be like <#1234>
    ch = message.content.split()[1]
    lench = len(ch)
    chid = ch[2:lench-1]
    if not chid.isdecimal():
      message.delete()
      await message.reply(f"**You cannot send a message to this channel**,<@{author.id}>")
      return
    chan = client.get_channel(int(chid))
    if chan.last_message_id is None:
      message.delete()
      await message.reply(f"We couldn't get most recent message due to either we don't have permission or the most recent message is deleted and its ID no longer valid",delete_after=sf.settings["deltime"])
      return
    mes = await chan.fetch_message(chan.last_message_id)
    await message.reply(f"The most recent message in <#{chid}>\n{mes.content}\nby **{str(mes.author)}**")
    return
  if debug and (msg.split()[0] == (pfx+cmds[5]) ):
    test.stop()
    return
  if debug and (msg.split()[0] == (pfx+cmds[6]) ):
    test.restart()
    return

             ###   END OF DEBUG ###
  if cmd and (msg.split()[0][len(pfx):] not in cmds):
    await message.add_reaction(emoji[5])
    txt = msg[len(pfx):].lstrip().replace(" ","+")
    link = f"https://translate.google.com.vn/translate_tts?ie=UTF-8&q={txt}&tl=en&client=tw-ob"
    embed=discord.Embed(title=f"**{msg[len(pfx):].lstrip().upper()}**", url=link, description="", color=0x00ff00)
    embed.set_thumbnail(url=client.user.display_avatar)
    embed.set_footer(text=f"{message.author}",icon_url=f"{message.author.display_avatar}")
    await message.channel.send(embed=embed,delete_after=sf.settings["deltime"])
    return

  if not cmd and ("gren " in msg):
    await message.add_reaction(emoji[0])
    await message.add_reaction(emoji[1])
    await message.add_reaction(emoji[2])
    await message.add_reaction(emoji[3])
    await message.add_reaction(emoji[4])
    await message.add_reaction(emoji[5])
    await message.channel.send("gren gren gren gren gren",delete_after=sf.settings["deltime"])
    return

  if cmd and (msg.split()[0] == pfx+cmds[3]):
    # channel format would be like <#1234>
    ch = message.content.split()[1]
    lench = len(ch)
    chid = ch[2:lench-1]
    fr = len(pfx)+len(cmds[3])+lench+1
    mes = message.content[fr:]
    await message.channel.send(f"<@{author.id}>\nsend \n{mes}\n**{ch}**\n**ID**:{chid}",delete_after=sf.settings["deltime"])
    chan = client.get_channel(int(chid))
    if chan is not None:
      await chan.send(mes)
      return
    message.delete()
    await message.reply(f"**You cannot send a message to this channel**,<@{author.id}>")
    return

# Actual start logging-in
client.run(TOKEN)
