from discord.ext import tasks
from base import client
from grendate import GrenDate

# temporary functionality 
from os import getenv
import requests

fb_t = getenv('fb_token')
fb_id = getenv('fb_page_id')
cnt = 0


ID_CHANNEL_CRONJOB = 971240750731890738

# A cronjob loops every 1 minute (get time send it in a specific channel)
@tasks.loop(minutes=1)
async def test():
 channel = client.get_channel(ID_CHANNEL_CRONJOB)
 year,month,day,month_name,hour,minute,meridiem = GrenDate().now()
 season = GrenDate(int(year),int(month),int(day)).season()
 sp = " "
 cur = f"\n\n{sp*26}{int(year)}/{month_name}/{day}\n\n{sp*16}\💙{sp*6}{hour}:{minute}{sp*2}{meridiem}{sp*6}\💙" 
 await channel.send(f"**{cur}**\n{sp*31}**{season}**",delete_after=59)


def FB():
 global cnt
 names =["رحمن","رحيم","ملك","قدوس","سلام","مؤمن","مهيمن","عزيز","غفار","وهاب","رازق","فتاح","عليم","باسط","رافع","معز","سميع","بصير","حكم","عدل","لطيف","خبير","عظيم","غفور","شكور","كبير","حفيظ","جليل","كريم","مجيب","واسع","حكيم","ودود","مجيد","باعث","شهيد","حق","وكيل","قوي","متين","ولي","حميد","مبدئ","معين","محيي","حي","قيوم","احد","صمد","قادر","مقتدر","مقدم","أول","آخر","ظاهر","باطن","ولي","متعالي","بر","عفو","رؤوف","مالك الملك","ذو الإجلال والإكرام"," مقسط","جامع","غني","مغني","نافع","نور","هادي","بديع","باقي","وارث"]
 lng = len(names)
 msg = f" يارب يا {names[cnt%lng]} اشتغل بقى انا تعبت"
 img = "https://picsum.photos/450/250"
 post_url = f"https://graph.facebook.com/{fb_id}/photos"
 data = { 'url': img, 'caption': msg }
 payload = {"access_token":fb_t}
 r = requests.post(url=post_url,params=payload ,data=data)


@tasks.loop(minutes=3)
async def post_reddit():
 global cnt
 global fb_id
 global fb_t
 subreddit = ['programmerhumor','aww','marvel']
 ss = len(subreddit)
 url1 = f'https://www.reddit.com/r/{subreddit[cnt%ss]}/random.json?include_over_18=off'
 r = requests.get(url1, headers = {'User-agent': 'yourbot'})
 vars = {'title':"",'url':""}
 for k,v in vars.items():
  vars[k] = r.json()[0]['data']['children'][0]['data'][k]

 msg = vars['title']

 url = f"https://graph.facebook.com/{fb_id}/photos"

 payload = {"access_token":fb_t}

 data = { 'url': vars['url'], 'caption': msg }
 try:
  z = requests.post(url,params=payload ,data=data)
  if z.status_code != 200:
   FB()
 except:
  print("Exception in post_reddit this request is CRAZY")
 cnt += 1



@client.event
async def on_ready():
 print(f"{client.user} has connected to Discord!\nHello World")
 print("------")
 try:
  post_reddit.start()
  print("test function is starting ...")
  await test.start()
 except Exception as e:
  print(f"Exception in on_ready check it fast\n{str(e)}")
