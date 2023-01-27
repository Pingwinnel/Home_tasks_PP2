#Arrays

cars = ["Ford", "Volvo", "BMW"]

print(cars) #['Ford', 'Volvo', 'BMW']

#Access the Elements of an Array

cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)   #Ford

cars = ["Ford", "Volvo", "BMW"]

cars[0] = "Toyota"

print(cars)  #['Toyota', 'Volvo', 'BMW']

#The Length of an Array
cars = ["Ford", "Volvo", "BMW"]

x = len(cars)

print(x)    #3

#Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)
#Ford
#Volvo
#BMW


#Adding Array Elements
cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)   #['Ford', 'Volvo', 'BMW', 'Honda']

#Removing Array Elements
cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)  #['Ford', 'BMW']


cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")

print(cars)   #['Ford', 'BMW']



