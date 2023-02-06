x=int(input())
i=1
j=1
for i in range(x+1):
    for j in range(i):
        if j==i-1:
            print(j+1,sep='')
        else:
            print(j+1,sep='',end='')
