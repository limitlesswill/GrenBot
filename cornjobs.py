from discord.ext import tasks
import datetime

ID_CHANNEL_CORNJOB = 971240750731890738

@client.event
async def on_ready():
 print(f"{client.user} has connected to Discord!\nHello World")
 test.start()
 print('------')
 print("test function has started")


# A cornjob loops every 1 minute (get time send it in a specific channel)
@tasks.loop(minutes=1)
async def test():
 channel = client.get_channel(ID_CHANNEL_CORNJOB)
 cur = datetime.datetime.utcnow().strftime("\t\t\t\t\t    %Y/%B/%d\n\n\t\t\t\t\t\💚  %I:%M  %p  \💚")
 await channel.send(f"\t\t\t\t\t**{cur}**",delete_after=59)
