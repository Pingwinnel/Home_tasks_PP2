x=input()
y=x.count('f')
if y==1:
    print(-1)
elif y==0:
    print(-2)
else:
    z=x.find('f')
    print(x.find('f',z+1))
