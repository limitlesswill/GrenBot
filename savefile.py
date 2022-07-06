from os import getenv
from dropbox import Dropbox


dbx = Dropbox(
 app_key = getenv('DROPBOX_APP_KEY'),
 app_secret = getenv('DROPBOX_APP_SECRET'),
 oauth2_refresh_token = getenv('DROPBOX_REFRESH_TOKEN')
 )

def download(from_file_server,to_file_local):
 global dbx
 with open(to_file_local,"wb") as f :
  metadata, r = dbx.files_download(from_file_server)
  f.write(r.content)
 return

def upload(from_file_server,to_file_local):
 global dbx
 file = open(to_file_local, "rb")
 dbx.files_upload(file.read(), from_file_server)
 file.close()
 return


"""
files would be :
ids:
^ this also contains categories of ids [developers , blocked users ,guilds , channels ] etc.

keywords:

commands:

others:

"""

class setting():

 file_ids = "/ids.txt"
 file_keywords = "/keywords.txt"
 file_commands = "/commands.txt"
 file_others = "/others.txt"
 
 devs = [333529891163340801]
 blok = []
 glds = [970576952257835059]
 chls = [971240750731890738]
 
 keywords={"gren ":"gren gren gren gren ","blu ":"blu blu blu","autocalendar":"no","tasktime":"1","deltime":"59"}
 
 commands=[".","save","load","peek","send","recent","timestop","timerestart"]
 others= ["https://www.google.com","time machine"]
 
 def peek():
  try:
   files = [setting.file_ids,setting.file_keywords,setting.file_commands,setting.file_others]
   
   txt = ""
   for file in files:
   
    download(file,file)
    
    tmp = open(file,"r")
    txt += tmp.read()    
    tmp.close()
    if len(txt):
     txt += "\n"
    
  except Exception as e:
   return 0,str(e)
  return txt.count("\n"),txt


# ORDER IS IMPORTANT ##

 def save_ids():
  try:
   lists = [setting.devs,setting.blok,setting.glds,setting.chls]
   a = "\n".join(str(x) for sub in lists for x in sub)
   
   lens = ",".join(str(len(x)) for x in lists)
   file = open(setting.file_ids,"w")
   file.write(f"{a}\n{lens}")
   file.close()
  except:
   return False

  return upload(setting.file_ids,setting.file_ids)
  

 def load_ids():
 
  download(setting.file_ids,setting.file_ids)
  
  try:
   file = open(setting.file_ids,"r")
   txt = file.read().split("\n")
   file.close()
  
   
   last_line = txt[len(txt)-1].split(",")
  
   lists = [setting.devs,setting.blok,setting.glds,setting.chls]
 
   lens = [int(x) for x in last_line]
   
 
   [x.clear() for x in lists]
   tmp = 0
   acc = lens[tmp]
   for x in range(len(txt)-1):
    if x >= acc:
     tmp += 1
     acc += lens[tmp]
   
    lists[tmp].append(int(txt[x]))
  except:
   return False
  return True

 
 def save_keywords():
  try:
   a = "\n".join(f"{x}:{y}" for x,y in setting.keywords.items())
   file = open(setting.file_keywords,"w")
   file.write(f"{a}")
   file.close()
  except:
   return False
  return upload(setting.file_keywords,setting.file_keywords)
  
 
 def load_keywords():
  download(setting.file_keywords,setting.file_keywords)
  
  try:
   txt = ""
   file = open(setting.file_keywords,"r")
   txt = file.read().split("\n")
   file.close()
   setting.keywords.clear()
  
   for x in txt:
    line = x.split(":")
    key=line[0]
    value=line[1]
    setting.keywords[key] = value
  except:
   return False
  return True


 def save_commands():
  try:
   a = "\n".join(x for x in setting.commands)
   file = open(setting.file_commands,"w")
   file.write(f"{a}")
   file.close()
  except:
   return False
  return upload(setting.file_commands,setting.file_commands)
  
  
 def load_commands():
  download(setting.file_commands,setting.file_commands)
  
  try:
   file = open(setting.file_commands,"r")
   txt = file.read().split("\n")
   file.close()
   setting.commands.clear()
   [setting.commands.append(x) for x in txt]
  except:
   return False
  return True


 def save_others():
  try:
   a = "\n".join(x for x in setting.others)
   file = open(setting.file_others,"w")
   file.write(f"{a}")
   file.close()
  except:
   return False
  return upload(setting.file_others,setting.file_others)
  
  
 def load_others():
  download(setting.file_others,setting.file_others)
  
  try:
   file = open(setting.file_others,"r")
   txt = file.read().split("\n")
   file.close()
   setting.others.clear()
   [setting.others.append(x) for x in txt]
  except:
   return False
  return True


# which:str can only be one of these values
#      ["devs","blok","glds","chls"]

 def add_ids(which:str,*args):
  target = 1
  if which == "devs":
   target = 0
  elif which == "glds":
   target = 2
  elif which == "chls":
   target = 3
  tmp = [setting.devs,setting.blok,setting.glds,setting.chls]
 
  try:
   for x in args:
    tmp[target].append(int(x))
  except:
   return False
  return setting.save_ids()


# which:str can only be one of these values
#      ["devs","blok","glds","chls"]

 def delete_ids(which:str,*args):

  target = 1
 
  if which == "devs":
   target = 0
  elif which == "glds":
   target = 2
  elif which == "chls":
   target = 3
  tmp = [setting.devs,setting.blok,setting.glds,setting.chls]
 
  for x in args:
   while x in tmp[target]:
    tmp[target].remove(x)
  return setting.save_ids()


# don't forget keyword argument **{key:value}

 def add_keywords(**args):

  for x in args:
   setting.keywords[x] = str(args[x])
  return setting.save_keywords()

 def delete_keywords(*args):
 
  for x in args:
   if x in setting.keywords:
    setting.keywords.pop(x)
  return setting.save_keywords()

 def edit_keywords(**args):

  for x in args:
   if x in setting.keywords:
    setting.keywords.pop(x)
    setting.keywords[x] = str(args[x])
  return setting.save_keywords()
 
## Only changes the name of a command

 def edit_commands(**args):
  for x in args:
   if x in setting.commands:
    setting.commands[setting.commands.index(x)] = str(args[x])
  return setting.save_commands()
    

 def add_others(*args):

  for x in args:
   setting.others.append(str(x))
  return setting.save_others()

 def delete_others(*args):
 
  for x in args:
   while x in setting.others:
    setting.others.remove(x)
  return setting.save_others()







