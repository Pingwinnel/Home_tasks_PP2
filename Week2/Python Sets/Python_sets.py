#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)    #{'cherry', 'banana', 'apple'}

# Note: the set list is unordered, meaning: the items will appear in a random order.

# Refresh this page to see the change in the result.

#Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) #{'banana', 'cherry', 'apple'}

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))  #3

#Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
#{'cherry', 'apple', 'banana'}
#{1, 3, 5, 7, 9}
#{False, True}

set1 = {"abc", 34, True, 40, "male"}

print(set1)  #{True, 34, 40, 'male', 'abc'}

#type()

myset = {"apple", "banana", "cherry"}

print(type(myset))  #<class 'set'>

#The set() Constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.
#{'banana', 'cherry', 'apple'}

#Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#banana
#cherry
#apple

#Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)           #{'cherry', 'apple', 'banana', 'orange'}

#Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)                #{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)         #{'banana', 'cherry', 'apple', 'orange', 'kiwi'}

#Remove Item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)       #{'cherry', 'apple'}


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)      #{'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal


thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)       #set()



#thisset = {"apple", "banana", "cherry"}

#del thisset

#print(thisset) #this will raise an error because the set no longer exists

#Loop Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
​
for x in thisset:
  print(x)
​
#cherry
#banana
#apple

#Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)   #{2, 1, 'b', 'c', 'a', 3}

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)   #{'a', 2, 3, 'c', 'b', 1}
 
 