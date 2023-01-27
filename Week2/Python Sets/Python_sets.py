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
