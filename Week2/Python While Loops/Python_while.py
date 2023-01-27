#The while Loop
i = 1
while i < 6:
  print(i)
  i += 1
#1
#2
#3
#4
#5

#The break Statement
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
#1
#2
#3

#The continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#1
#2
#4
#5
#6

# Note that number 3 is missing in the result


#The else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#1
#2
#3
#4
#5
#i is no longer less than 6