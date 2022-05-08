from os import getenv
from dropbox import Dropbox

file_name = "settings.ini"
server_name = "/settings.ini"
settings = {"deltime":20,"intval":6}

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


def save():
 global file_name
 global server_name
 global settings
 file = open(file_name,"w")
 for key,value in settings.items():
  file.write(f"{key}:{value}\n")
 file.close()
 upload(server_name,file_name)
 return

def load():
 global file_name
 global settings
 global server_name
 download(server_name,file_name)
 newdic = {}
 file = open(file_name,"r")
 for line in file:
  key=line.split(":")[0]
  value=line.split(":")[1]
  newdic[key] = int(value)
 settings = newdic
 file.close()
 return

def peek():
 global file_name
 file = open(file_name,"r")
 txt = ""
 for line in file:
  txt += line
 file.close()
 return txt


