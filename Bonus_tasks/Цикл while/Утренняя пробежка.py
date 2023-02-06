x=int(input())
y=int(input())
sum=x
i=1
while sum<y:
    sum=sum+sum/10
    i=i+1
else:
    print(i)
