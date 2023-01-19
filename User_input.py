flag=False
while(flag!=True): 
  try :username=int(input("Enter your age:"))
  except ValueError: print("Enter digit !")
  else:flag=True       


print("Your age :",username)