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
pfx = "."
cmds = {0:"join",1:"leave",2:"web"}

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

  if msg == pfx+cmds[1]:
    await message.reply(f"**message.guild.voice_client**\n{message.guild.voice_client}**Ends here**")
      if message.guild.VoiceClient is None:
        await message.reply("I'm not even in a voice channel")
        return
      else:
        await message.reply(f"**Data After voice_client is not None AKA message.guild.voice_client :**\n{message.guild.voice_client}**Ends here**")
        await message.guild.voice_client.disconnect()
        await message.add_reaction(emoji[1])
        await message.reply("See you later")
    
  if msg == pfx+cmds[0]:
    if author.voice is None:
      await message.reply("You are not in a **Voice Channel**")
      return
    else:
      await message.reply(f"**Data**\nauthor.voice.channel.id:\n{author.voice.channel.id}\nmessage.voice_client.channel.id\n{message.voice_client.channel.id}")
        if author.voice.channel.id != message.voice_client.channel.id:
          await message.guild.voice_client.move_to(message.author.voice.channel)
          await message.reply(f"Wait for me , I'm comming to {author.voice.channel.name}\n")
        else:
          await author.voice.channel.connect()
          await message.add_reaction(emoji[4])
          await message.add_reaction(emoji[1])
          await message.reply("**I'm Connecting...**",mention_author=False)

  if msg == pfx+cmds[2]:
    await obj = hweb()
    await message.reply(obj.get_data())

  if msg.startswith(pfx) and msg[1:] not in cmds :
    rpl = f"I\'m currently under-development , {author} \n please try again later \n Your message content was \n ```{message.content}```\n"  
    await message.reply(rpl)
    await message.add_reaction(emoji[1])
     

# Actual start logging-in
client.run(TOKEN)
