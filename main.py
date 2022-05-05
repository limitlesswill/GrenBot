import os
import savefile as sf
import discord

# Loading TOKEN from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

intent = discord.Intents(messages=True, guilds=True)
intent.reactions = True
intent.message_content = True
intent.typing = False
intent.presences = False

# Instantiate an object of the client
client = discord.Client(intents=intent)

# Prefix of the bot
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
  emoji = ["👀","👋","👉","👈","👍","💚"]
    
  if msg == pfx and (str(author) == "User#3231"):
    gds = [x.name for x in client.guilds]
    await message.reply( "\n".join(gds),delete_after=sf.settings["deltime"])
    await message.add_reaction(emoji[1])
    await message.add_reaction(emoji[2])
    await message.add_reaction(emoji[3])
    sf.save()
    txt = sf.peek()
    await message.channel.send(txt)
    return

  if cmd and (msg.split()[0][len(pfx):] not in cmds):
    await message.add_reaction(emoji[5])
    txt = msg[len(pfx):].lstrip().replace(" ","+")
    link = f"https://translate.google.com.vn/translate_tts?ie=UTF-8&q={txt}&tl=en&client=tw-ob"
    embed=discord.Embed(title=f"**{msg[len(pfx):].lstrip().upper()}**", url=link, description="", color=0x00ff00)
    embed.set_thumbnail(url=client.user.display_avatar)
    embed.set_footer(text=f"{message.author}",icon_url=f"{message.author.display_avatar}")
    await message.reply(embed=embed)
    await message.reply("https://media.discordapp.net/attachments/970599884157751306/971337061976125520/FB_IMG_1648960892703.jpg")
    return

  if "gren " in msg:
    await message.add_reaction(emoji[0])
    await message.add_reaction(emoji[1])
    await message.add_reaction(emoji[2])
    await message.add_reaction(emoji[3])
    await message.add_reaction(emoji[4])
    await message.add_reaction(emoji[5])
    await message.channel.send("gren")
    return

# Actual start logging-in
client.run(TOKEN)
