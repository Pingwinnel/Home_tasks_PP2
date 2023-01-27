fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)   #"apple", "banana", "cherry"
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    
     continue
print(x)      #apple,cherry

for x in range(6):
 print(x)   
#0
#1
#2
#3
#4
#5

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    
     break

  print(x)         #"apple"