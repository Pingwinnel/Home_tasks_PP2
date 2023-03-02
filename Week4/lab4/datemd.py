import datetime 
#1ex
x=datetime.datetime.now()
old_time=x+datetime.timedelta(days=-5)
print(old_time)
#2ex
today=datetime.datetime.now()
yes_day=today+datetime.timedelta(days=-1)
tomorro=today+datetime.timedelta(days=1)
print("Yesterday:",yes_day, "\nToday:",today,"\nTommorow:",tomorro)
#3ex
print(today.strftime("%f"))
#4ex
from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
year=input("Year: ")
mount=input("Month: ")
day=input("Day: ")
hour=input("Hour: ")
minute=input("Minute: ")
second=input("Seconds: ")
date1 = datetime.strptime(f'{year}-{mount}-{day} {hour}:{minute}:{second}', '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
