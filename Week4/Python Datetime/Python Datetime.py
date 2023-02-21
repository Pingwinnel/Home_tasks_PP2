import datetime

x = datetime.datetime.now()

print(x)

#Date Output
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))  
#2023
#Tuesday

#Creating Date Objects
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)        
#2020-05-17 00:00:00

#The strftime() Method

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
#June

