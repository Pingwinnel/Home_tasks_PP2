import re
user_input=input("Input some string: ")
#1ex
x1=re.search("[a]",user_input)
if x1:
    print("Yes! We have a match")
else:
    print("No match")
#2ex
x2=re.search("abb",user_input)
if x2:
    print("Yes! We have a match")
else:
    print("No match")
#3ex
x3=re.search("[a-z]+_+[a-z]",user_input)
if x3:
    print("Yes! We have a match")
else:
    print("No match")   
#4ex
x4=re.search("[A-Z]+[a-z]",user_input)
if x4:
    print("Yes! We have a match")
else:
    print("No match")
#5ex
x5=re.search("^a...b",user_input)
if x5:
    print("Yes! We have a match")
else:
    print("No match")
#6ex
x6=re.sub("\.|\ |,",":",user_input)
print(x6)
#7ex
x7=re.split("_",user_input)
z=""
y=""
for word in x7:
    z=z+y.join(word.capitalize())
print(z)
#8ex
x8=re.split("[A-Z]",user_input)
print(x8)
#9ex
x9=re.sub(r"(\w)([A-Z])",r"\1 \2", user_input)
print(x9)
#10ex
x10=re.sub(r"(\w)([A-Z])",r"\1_\2",user_input)
print(x10)
