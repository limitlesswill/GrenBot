import discord
from discord import app_commands
from typing import Optional
from base import client


@client.tree.command()
async def hello(interaction: discord.Interaction):
 """Says hi!"""
 await interaction.response.send_message(f'Hi, {interaction.user.mention}')


@client.tree.command()
@app_commands.describe(
 first_value='The first value you want to add something to',
 second_value='The value you want to add to the first value')

async def multi(interaction: discord.Interaction, first_value: int, second_value: int):
 """Multiplying two numbers together."""
 await interaction.response.send_message(f'{first_value} * {second_value} = {first_value * second_value}',ephemeral=True)


# The rename decorator allows us to change the display of the parameter on Discord.
# In this example, even though we use `text_to_send` in the code, the client will use `text` instead.
# Note that other decorators will still refer to it as `text_to_send` in the code.
@client.tree.command()
@app_commands.rename(text_to_send='text')
@app_commands.describe(text_to_send='Text to send in the current channel')
async def send(interaction: discord.Interaction, text_to_send: str):
 """Sends the text into the current channel."""
 await interaction.response.send_message(text_to_send+"\n**interaction.channel** :\n"+str(interaction.channel))


# To make an argument optional, you can either give it a supported default argument
# or you can mark it as Optional from the typing standard library. This example does both.
@client.tree.command()
@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
 """Says when a member joined."""
 # If no member is explicitly provided then we use the command user here
 member = member or interaction.user
 # The format_dt function formats the date time into a human readable representation in the official client
 await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')
