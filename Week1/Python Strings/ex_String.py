x = "Hello World"
print(len(x))  #11

txt = "Hello World"
x = txt[0]   #H

txt = "Hello World"
x = txt[2:5]   #llo

txt = " Hello World "
x = txt.strip()   #HelloWorld

txt = "Hello World"
txt = txt.upper()   #HELLO WORLD

txt = "Hello World"
txt = txt.lower()   #hello world

txt = "Hello World"
txt = txt.replace('H', 'J')  #Jello World

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))       #My name is John, and I am 36

