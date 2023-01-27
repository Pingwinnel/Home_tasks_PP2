fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#apple 
# banana 
# cherry

#Looping Through a String
for x in "banana":
  print(x) 
#b
#a
#n
#a
#n
#a

#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
#apple
#banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)   #apple
  
#The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
#apple
#cherry

#The range() Function
for x in range(6):
  print(x) 
#0
#1
#2
#3
#4
#5

for x in range(2, 6):
  print(x) 
#2
#3
#4
#5

for x in range(2, 30, 3):
  print(x) 
#2
#5
#8
#11
#14
#17
#20
#23
#26
#29


#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!") 
#0
#1
#2
#3
#4
#5
#Finally finished!

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed
#0
#1
#2


#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#red apple
#red banana
#red cherry
#big apple
#big banana
#big cherry
#tasty apple
#tasty banana
#tasty cherry


#The pass Statement
#for x in [0, 1, 2]:
#  pass

# having an empty for loop like this, would raise an error without the pass statement
