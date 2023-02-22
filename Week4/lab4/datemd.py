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
year1=input("year")
day1=input("Day")
mounth1=input("mounth")
