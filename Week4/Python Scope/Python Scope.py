#Local Scope
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function
def myfunc():
  x = 300
  print(x)

myfunc()         #300

#Function Inside Function
#As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()    #300


#Global Scope
x = 300

def myfunc():
  print(x)

myfunc()    #300

print(x)    #300

#Naming Variables
#If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()     #200

print(x)     #300

#Global Keyword
def myfunc():
  global x
  x = 300

myfunc()

print(x)   #300

x = 300



def myfunc():
  global x
  x = 200

myfunc()

print(x)         #200





