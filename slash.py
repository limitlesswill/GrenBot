import discord
from discord import app_commands
from base import client
from savefile import setting


@client.tree.command()
@app_commands.describe(id="Enter any valid Discord ID")
async def date(interaction: discord.Interaction, id: str = "1420070400000"):
 """Prints Time that ID created at"""

 if interaction.user.id in setting.blok:
  return
 setting.add_users(interaction.user.id)

 if len(id) < 18:
  await interaction.response.send_message(f"please enter a valid Discord ID",ephemeral=True)
 DISCORD_EPOCH = 1420070400000
 milliseconds = (int(id) >> 22) + DISCORD_EPOCH
 milliseconds = int(milliseconds/1000)
 await interaction.response.send_message(f"{milliseconds}\n<t:{milliseconds}:F>")

@client.tree.command()
async def join(interaction: discord.Interaction):
 """Joins you in Voice channel"""

 if interaction.user.id in setting.blok:
  return
 setting.add_users(interaction.user.id)

 vc = interaction.user.voice
 if vc:
  await interaction.response.send_message(f"{interaction.user.mention} I have joined you in {str(vc)}",ephemeral = True)
  await vc.channel.connect()
 else:
  await interaction.response.send_message(f"Please join a voice channel then i will follow you,\n{interaction.user.mention}",ephemeral=True)

@client.tree.command()
@app_commands.describe(
 first_value='The first value you want to add something to',
 second_value='The value you want to add to the first value')

async def multi(interaction: discord.Interaction, first_value: int, second_value: int):
 """Multiplying two numbers together."""

 if interaction.user.id in setting.blok:
  return
 setting.add_users(interaction.user.id)

 await interaction.response.send_message(f'{first_value} * {second_value} = {first_value * second_value}',ephemeral=True)


# The rename decorator allows us to change the display of the parameter on Discord.
# In this example, even though we use `text_to_send` in the code, the client will use `text` instead.
# Note that other decorators will still refer to it as `text_to_send` in the code.
@client.tree.command()
@app_commands.rename(text_to_send='text')
@app_commands.describe(text_to_send='Text to send in the current channel',channel="for testing purposes only")
async def send(interaction: discord.Interaction, text_to_send: str, channel: Optional[discord.TextChannel] = None):
 """Sends the text into a channel."""

 if interaction.user.id in setting.blok:
  return
 setting.add_users(interaction.user.id)

 if channel:
  await channel.send(text_to_send)
  await interaction.response.send_message(f"{interaction.user.mention}, your message has been went to {str(channel)}",ephemeral=True)
 else:
  await interaction.response.send_message(text_to_send)


# To make an argument optional, you can either give it a supported default argument
# or you can mark it as Optional from the typing standard library. This example does both.
@client.tree.command()
@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
 """Says when a member joined."""

 if interaction.user.id in setting.blok:
  return
 setting.add_users(interaction.user.id)

 # If no member is explicitly provided then we use the command user here
 member = member or interaction.user
 # The format_dt function formats the date time into a human readable representation in the official client
 await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')
