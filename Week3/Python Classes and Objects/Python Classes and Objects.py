#Create a Class

class MyClass:
  x = 5

print(MyClass)   #<class '__main__.MyClass'>

#Create Object

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)    #5

#The __init__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)    

print(p1.name)   #John
print(p1.age)    #36

#The __str__() Function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
 
print(p1)          #<__main__.Person object at 0x15039e602100>


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("John", 36)

print(p1)         #John(36)


#Object Methods

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()       #Hello my name is John


#The self Parameter
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()           #Hello my name is John


#Modify Object Properties

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)      #40


#Delete Object Properties
'''''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

print(p1.age)            #AttributeError: 'Person' object has no attribute 'age'
'''


'''''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)        #NameError: 'p1' is not defined
'''

#The pass Statement
class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement    
