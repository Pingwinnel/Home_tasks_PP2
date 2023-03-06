path="A.txt"
#1ex
read_=open(path,"r")
print(read_.read())
#2ex
import os
print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))
 #3ex
print('Exist:', os.access(path, os.F_OK))
if os.access(path,os.F_OK)==True:
    f=open(path)
    print(f.read())
     
#4ex
f=open(path,"rt")
count=0
for i in f:
    count+=1
print(count)
#5ex
list=[1,2,'apple']
f=open(path,"a")
for i in list:
    f.write(str(i))
f.close()
f=open(path)
print(f.read())
#6ex
for i in range(26):
    num=65+i
    char=chr(num)
    try:
        f=open(f"{char}.txt","x")
    except IOError as error:
        pass
#7ex
path1="A.txt"
path2="B.txt"
f=open(path1,"r")
f1=open(path2,"w")
f1.write(f.read())
#8ex
path3="C.txt"
print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))
if os.access(path, os.F_OK)==True:
    os.remove(path3)
    print("File succesful deleted")
else:
    print("no such file in directory")