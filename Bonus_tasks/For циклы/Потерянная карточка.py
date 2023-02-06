x=int(input())
i=0
lis=[]
for i in range(x-1):
    y=int(input())
    lis.append(y)
n=1
for j in range(x):
    if n in lis:
        j=j+1
        n=n+1
    else:
        print(n)
        break
