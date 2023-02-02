#Creating a Function
def my_function():
  print("Hello from a function") 
  
#Calling a Function
def my_function():
  print("Hello from a function")  

my_function()    #Hello from a function

#Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")    #Emil Refsnes
my_function("Tobias")  #Tobias Refsnes
my_function("Linus")   #Linus Refsnes




#Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")    #Emil Refsnes


def my_function(fname, lname):
  print(fname + " " + lname)

#my_function("Emil")    #This function expects 2 arguments, but gets only 1

#ERROR



#Arbitrary Arguments, *args

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")   #The youngest child is Linus



#Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")   #The youngest child is Linus


#Arbitrary Keyword Arguments, **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")   #His last name is Refsnes


#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")     ##I am from Sweden
my_function("India")      ##I am from India
my_function()             #I am from Norway
my_function("Brazil")     #I am from Brazil


#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)#apple  banana  cherry

#Return Values
def my_function(x):
  return 5 * x

print(my_function(3))#15
print(my_function(5))#25
print(my_function(9))#45

#The pass Statement
def myfunction():
  pass

# having an empty function definition like this, would raise an error without the pass statement


#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
#Recursion Example Results
#1
#3
#6
#10
#15
#21






