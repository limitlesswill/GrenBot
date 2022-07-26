from discord.ext import tasks
from base import client
from grendate import GrenDate
from savefile import setting



# A cornjob loops every 1 minute (get time send it in a specific channel)
@tasks.loop(minutes=int(setting.settings["tasktime"]))
async def test():
 for ID_CHANNEL_CORNJOB in setting.chls:

  channel = client.get_channel(ID_CHANNEL_CORNJOB)
  year,month,day,month_name,hour,minute,meridiem = GrenDate().now()
  season = GrenDate(int(year),int(month),int(day)).season()
  sp = " "
  cur = f"\n\n{sp*26}{int(year)}/{month_name}/{day}\n\n{sp*16}\💙{sp*6}{hour}:{minute}{sp*2}{meridiem}{sp*6}\💙"  
  await channel.send(f"**{cur}**\n{sp*29}**{season}**",delete_after=int(setting.settings["deltime"]))


@client.event
async def on_ready():
 print(f"{client.user} has connected to Discord!\nHello World")
 
 setting.load_ids()
 setting.load_settings()
 setting.load_commands()
 setting.load_others()

 if setting.settings["autocalendar"] == "yes":
  print("------\ntest function is starting ...")
  await test.start()

