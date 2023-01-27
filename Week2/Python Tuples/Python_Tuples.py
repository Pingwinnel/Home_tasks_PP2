#tuple syntax
mytuple = ("apple", "banana", "cherry")

thistuple = ("apple", "banana", "cherry")
print(thistuple)   ##('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)   #('apple', 'banana', 'cherry', 'apple', 'cherry')

#Tuple Length

thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))  #3
#Tuple Items
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#Since tuples are indexed, they can have items with the same value:

#Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))   #<class 'tuple'>
                         #<class 'str'>
#Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)
#('apple', 'banana', 'cherry')
#(1, 5, 7, 9, 3)
#(True, False, False)

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)  #('abc', 34, True, 40, 'male')

mytuple = ("apple", "banana", "cherry")

print(type(mytuple))  #<class 'tuple'>
#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)  #('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  #banana


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])  #cherry



thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])   #('cherry', 'orange', 'kiwi')

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[:4])  #('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[2:])   #('cherry', 'orange', 'kiwi', 'melon', 'mango')

#Range of Negative Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])  #('orange', 'kiwi', 'melon')

#Negative indexing means starting from the end of the tuple.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,


#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")                     #Yes, 'apple' is in the fruits tuple


#Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)   #("apple", "kiwi", "cherry")

#Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)        #('apple', 'banana', 'cherry', 'orange')


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)    #('apple', 'banana', 'cherry', 'orange')

#Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)          #('banana', 'cherry')


#thistuple = ("apple", "banana", "cherry")
#del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists


#Traceback (most recent call last):
#  File "demo_tuple_del.py", line 3, in <module>
#    print(thistuple) #this will raise an error because the tuple no longer exists
#NameError: name 'thistuple' is not defined


#Unpacking a Tuple

fruits = ("apple", "banana", "cherry")

print(fruits)


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)           #apple
print(yellow)          #banana
print(red)             #cherry

#Using Asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)#apple

print(yellow)#banana
print(red)#['cherry', 'strawberry', 'raspberry']    



fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)         #apple
print(tropic)        #['mango', 'papaya', 'pineapple']
print(red)           #cherry

#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#apple
#banana
#cherry


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
#apple
#banana
#cherry

#Join Two Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)             #('a', 'b', 'c', 1, 2, 3)


#Multiply Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)    #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
