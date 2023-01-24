x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
#int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
#it is also float
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
#complex numbers
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Type Conversion
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))
#You cannot convert complex numbers into another number type.

#Random Number
import random

print(random.randrange(1, 10))
