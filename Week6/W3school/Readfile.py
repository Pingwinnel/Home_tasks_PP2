#Open a File on the Server

f = open("demofile.txt", "r")

print(f.read())
#Hello! Welcome to demofile.txt
#This file is for testing purposes.
#Good Luck!

f = open("D:\\myfiles\welcome.txt", "r")

print(f.read())
#Welcome to this text file!
#This file is located in a folder named "myfiles", on the D drive.
#Good Luck!

#Read Only Parts of the File
f = open("demofile.txt", "r")

print(f.read(5))   #Hello


#Read Lines
f = open("demofile.txt", "r")

print(f.readline())    #Hello! Welcome to demofile.txt


f = open("demofile.txt", "r")

print(f.readline())
print(f.readline())
#Hello! Welcome to demofile.txt
#This file is for testing purposes.


f = open("demofile.txt", "r")
for x in f:
  print(x)

#Hello! Welcome to demofile.txt
#This file is for testing purposes.
#Good Luck!

#Close Files
f = open("demofile.txt", "r")

print(f.readline())           #Hello! Welcome to demofile.txt

f.close()

