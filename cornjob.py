from discord.ext import tasks
from datetime import datetime
from base import client

ID_CHANNEL_CORNJOB = 971240750731890738

"""
# ready to convert them into other calendars
import datetime
time = datetime.datetime.utcnow()
year = int(time.strftime("%Y"))+5
month = time.strftime("%m")
day = time.strftime("%d")
hour = time.strftime("%H")
minute = time.strftime("%M")
second = time.strftime("%S")
"""

# A cornjob loops every 1 minute (get time send it in a specific channel)
@tasks.loop(minutes=1)
async def test():
 channel = client.get_channel(ID_CHANNEL_CORNJOB)
 cur = datetime.utcnow().strftime("\n\n\t\t\t\t\t   %Y/%B/%d\n\n\t\t\t\t\t\💚    %I:%M  %p    \💚")
 await channel.send(f"\t\t\t\t\t**{cur}**",delete_after=59)


@client.event
async def on_ready():
 print(f"{client.user} has connected to Discord!\nHello World")
 await test.start()
 print('------')
 print("test function has started")
