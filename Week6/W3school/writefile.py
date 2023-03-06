#Write to an Existing File
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#Hello! Welcome to demofile2.txt
#This file is for testing purposes.
#Good Luck!Now the file has more content!

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())     #Woops! I have deleted the content!


#Create a New File
f = open("myfile.txt", "x")

f = open("myfile.txt", "w")
