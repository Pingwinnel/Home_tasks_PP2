#String format()

price = 49
txt = "The price is {} dollars"
print(txt.format(price))
#use format() and {}  to add variables into string
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

#Multiple Values
#If you want to use more values, just add more values to the format() method:

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#Index numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

#Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
