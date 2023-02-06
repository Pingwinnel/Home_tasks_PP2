x=input()
y=x.count('f')
if y==1:
    print(x.find('f'))
elif y>=2:
    print(x.find('f'),x.rfind('f'))
