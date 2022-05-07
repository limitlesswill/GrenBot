import dropbox

file_name = "settings.ini"
settings = {"deltime":20,"intval":6}
dbx = dropbox.Dropbox(os.getenv('DROPBOX_TOKEN'))

def save():
 global dbx
 global file_name
 global settings
 file = open(file_name,"w")
 for key,value in settings.items():
  file.write(f"{key}:{value}\n")
 file.close()
 dbx.files_upload(file.read(), filename, mute=True)

def load():
 global dbx
 global file_name
 global settings
 f, r = dbx.files_download(file_name)
 newdic = {}
 for line in r.content:
  key=line.split(":")[0]
  value=line.split(":")[1]
  newdic[key] = int(value)
 settings = newdic
 f.close()

def peek():
 global file_name
 file = open(file_name,"r")
 txt = ""
 for line in file:
  txt += line
 file.close()
 return txt


