import datetime

class GrenDate():
 def __init__(self,year:int=1,month:int=1,day:int=1):
  self.error = year < 1 or month < 1 or day < 1 or month > 10 or (day > (14 if month%2 else 16))
  self.day = day
  self.month = month
  self.year = year
  self.monthname = ["0","Salar","Hurze","Malini","Malze","Palar","Polar","Vensa","Duren","Zenshin","Solar"] 
  if self.error:
   self.year,self.month,self.day = 0,0,0

 def __str__(self):
  return f"{self.year}/{self.monthname[self.month]}/{self.day}"

########### date STARTS at 1/1/1 ###########
 def to_days(self):
  if self.error or self.year < 1 or self.month < 1 or self.day < 1:
   return 0 
  return ( (self.year - 1) * 150) + ( (self.month-1) * 15 - ( (self.month-1)%2) ) + self.day
  
######### returns (YEAR,MONTH,DAY) #########
 def to_date(self,s:int):
  if s < 1:
   return 0,0,0  
  y = int(s/150)
  s = s - (y * 150)
  m = int(s/15)
  d = s - (m*15) + (m%2)
  y += 1
  m += 1
  if not d :
   d = 16
   m -= 1
  if not m:
   m = 10
   y -= 1
  return y,m,d

### accumelative calculating the seasons ####
 def season(self):
  duration = [25,25,50,25,25]
  name = ["Durea","Polea","Selena","Late Polea","Late Durea"]  
# convert date to days starting from the current year (seasons don't change)
  sd = GrenDate(1,self.month,self.day).to_days()
  tmp = 0
  for x in range(len(duration)):
   tmp += duration[x]
   if sd <= tmp:
    return name[x]   
  self.error = True
  return self.error

## adding years or months or days to 1/1/1 ##
 def add(self,years:int=0,months:int=0,days:int=0):
  if years < 0 or months < 0 or days < 0:
   return 0,0,0
  stamp = 1
  stamp += years*150
  stamp += days
  stamp += ( months * 15 ) - ( months % 2 )
  stamp += self.to_days()-1
  return self.to_date(stamp)
  
###   returns updated variables ###
###         Tuple of strings    ### 
###         1- year             ### 
###         2- month            ### 
###         3- day              ### 
###         4- month name       ### 
###         5- hour             ### 
###         6- minute           ### 
###         7- meridiem         ### 

 def now(self):
  epoch = datetime.datetime(2022,5,2) 
  current = datetime.datetime.utcnow()+datetime.timedelta(hours = 8) 
  dif_day = (current-epoch).days
  year,month,day = GrenDate().add(days=dif_day)
  monthname = self.monthname[month]
  hour = current.strftime("%I")
  minute = current.strftime("%M")
  pm = current.strftime("%p")
  return str(year).zfill(4),str(month).zfill(2),str(day).zfill(2),monthname,hour,minute,pm



