file_name = "settings.ini"
settings = {"deltime":30,"intval":6}

def save():
 global file_name
 global settings
 file = open(file_name,"w")
 for key,value in stg.items():
  file.write(f"{key}:{value}\n")
 file.close()

def load():
 global file_name
 global settings
 newdic = {}
 file = open(file_name,"r")
 for line in file:
  key=line.split(":")[0]
  value=line.split(":")[1]
  newdic[key] = int(value)
 stg = newdic
 file.close()

def peek():
 global file_name
 file = open(file_name,"r")
 txt = file.readlines()
 file.close()
 return txt

