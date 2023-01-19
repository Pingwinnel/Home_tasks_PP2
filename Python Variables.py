x = 7
y = "John"
print(x)
print(y)
 
x = 5       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

#Type function
x = 5
y = "John"
print(type(x))   #class <int>
print(type(y))   #class <str>

x = "John"
print(x)
# is the same as
x = 'John'
print(x)


a = 4
A = "Sally"
#A and a another variables 
print(a)
print(A)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# 2myvar = "John"
# my-var = "John"
# my var = "John"

#This example will produce an error in the result

#There some case to make variables more readable 

#Camel Case : Each word, except the first, starts with a capital letter
myVariableName = "John"
#Pascal Case : Each word starts with a capital letter
MyVariableName = "John"
#Snake Case : Each word is separated by an underscore character
my_variable_name = "John"

#Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)
 # !Note: Make sure the number of variables matches the number of values, or else you will get an error.!

#And you can assign the same value to multiple variables in one line
x = y = z = "Orange"
print(x)
print(y)
print(z)
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

#Print function
x = "Python is awesome"
print(x)
#In the print() function, you output multiple variables, separated by a comma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#You can also use the + operator to output multiple variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Global variables

#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)