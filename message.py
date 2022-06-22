import discord
from base import client
import savefile as sf
from cornjob import test

# Prefix of the bot
pfx = "."
cmds = ["save","load","peek","send","recent","timestop","timerestart"]

@client.event
async def on_message(message):
  if message.author.bot:
    return

# (DM message handling)
  if message.guild is None:
#    embed=discord.Embed(title="Invite me to your **server**", url="https://discordapp.com/oauth2/authorize?client_id=569724616210382875&scope=bot&permissions=277129284672", description="", color=0x00ff00)
#    embed.set_author(name=f"{message.author}", url="https://discordapp.com/oauth2/authorize?client_id=569724616210382875&scope=bot&permissions=277129284672", icon_url=f"{message.author.display_avatar}")
#    embed.set_thumbnail(url=client.user.display_avatar)
#    embed.set_footer(text=f"I'm a nice bot under construction")
#    await message.reply(embed=embed)
    return

  msg = message.content.lower()
  cmd = msg.startswith(pfx)
  author = message.author
  debug = (str(author) == "User#3231")
  emoji = ["👀","👋","👉","👈","👍","💚"]

             ###   START OF DEBUG ###

# Prefix only (print all guilds then disappear)
  if debug and (msg == pfx):
    gds = [x.name for x in client.guilds]
    await message.reply( "\n".join(gds),delete_after=sf.settings["deltime"])
    await message.add_reaction(emoji[1])
    await message.add_reaction(emoji[2])
    await message.add_reaction(emoji[3])
    return

# Saving settings to file
  if debug and (msg == (pfx+cmds[0]) ):
    sf.save()
    await message.reply("**Saved**",delete_after=sf.settings["deltime"])
    return

# Loading settings from file
  if debug and (msg == (pfx+cmds[1]) ):
    sf.load()
    await message.reply("**Loaded**",delete_after=sf.settings["deltime"])
    return

# Peeking on current file stats 
  if debug and (msg == (pfx+cmds[2])):
    await message.channel.send(f"file name: {sf.file_name}",delete_after=sf.settings["deltime"])
    await message.reply(f"**Data**: {sf.peek()}",delete_after=sf.settings["deltime"])
    await message.reply("**Peek**",delete_after=sf.settings["deltime"])
    return

# Getting the most recent message from channels handling
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

# Stoping cornjob
  if debug and (msg.split()[0] == (pfx+cmds[5]) ):
    test.stop()
    return

# Restarting cornjob
  if debug and (msg.split()[0] == (pfx+cmds[6]) ):
    test.restart()
    return

             ###   END OF DEBUG ###

# Text-to-speech if it isn't a command
  if cmd and (msg.split()[0][len(pfx):] not in cmds):
    await message.add_reaction(emoji[5])
    txt = msg[len(pfx):].lstrip().replace(" ","+")
    link = f"https://translate.google.com.vn/translate_tts?ie=UTF-8&q={txt}&tl=en&client=tw-ob"
    embed=discord.Embed(title=f"**{msg[len(pfx):].lstrip().upper()}**", url=link, description="", color=0x00ff00)
    embed.set_thumbnail(url=client.user.display_avatar)
    embed.set_footer(text=f"{message.author}",icon_url=f"{message.author.display_avatar}")
    await message.channel.send(embed=embed,delete_after=sf.settings["deltime"])
    return

# Respond if message contains "gren "
  if not cmd and ("gren " in msg):
    await message.add_reaction(emoji[0])
    await message.add_reaction(emoji[1])
    await message.add_reaction(emoji[2])
    await message.add_reaction(emoji[3])
    await message.add_reaction(emoji[4])
    await message.add_reaction(emoji[5])
    await message.channel.send("gren gren gren gren gren",delete_after=sf.settings["deltime"])
    return

# Respond to mention
  if client.user.mentioned_in(message):
    await message.reply(f"I work with **commands** not mentions 😒 \nhere is my fast growing list\n**{str(cmds)}**",delete_after=sf.settings["deltime"])

# Send a message to another channel
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

# Response to other memeber whom try to debug
  if cmd and not debug and (msg.split()[0][len(pfx):] in cmds):
    await message.add_reaction(emoji[0])
    await message.reply("What are you trying to do?")
    await message.channel.send(f"**Hey** <@{333529891163340801}>\nLook what <@{message.author.id}> have sent to me.\n**{message.content}**")


