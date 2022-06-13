from discord.ext import tasks
from base import client
import grendate

ID_CHANNEL_CORNJOB = 971240750731890738

# A cornjob loops every 1 minute (get time send it in a specific channel)
@tasks.loop(minutes=1)
async def test():
 channel = client.get_channel(ID_CHANNEL_CORNJOB)
 year,month,day,month_name,hour,minute,meridiem = GrenDate().now()
 season = GrenDate(year,month,day).season()
 cur = f"\n\n\t\t\t\t\t    {year}/{month_name}/{day}\n\n\t\t\t\t\t\💚    {hour}:{minute}  {meridiem}    \💚")
 await channel.send(f"\t\t\t\t\t**{cur}**\n\t\t\t\t\t{season}",delete_after=59)


@client.event
async def on_ready():
 print(f"{client.user} has connected to Discord!\nHello World")
 print('------')
 print("test function is starting ...")
 await test.start()

