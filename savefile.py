import os
import dropbox

file_name = "settings.ini"
server_name = "/settings.ini"
settings = {"deltime":20,"intval":6}
dbx = dropbox.Dropbox(os.getenv('DROPBOX_TOKEN'))

def save():
 global dbx
 global file_name
 global server_name
 global settings
 file = open(file_name,"w")
 for key,value in settings.items():
  file.write(f"{key}:{value}\n")
 file.close()
 dbx.files_upload(open(file_name, "rb").read(), server_name)

def load():
 global dbx
 global file_name
 global server_name
 global settings
 with open(file_name,"wb") as f :
  metadata, r = dbx.files_download(server_name)
  f.write(r.content)
 newdic = {}
 file = open(file_name,"r")
 for line in file:
  key=line.split(":")[0]
  value=line.split(":")[1]
  newdic[key] = int(value)
 settings = newdic
 file.close()

def peek():
 global file_name
 file = open(file_name,"r")
 txt = ""
 for line in file:
  txt += line
 file.close()
 return txt


