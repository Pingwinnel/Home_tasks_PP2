x=int(input())
i=0
while 2**i<=x:
    i=i+1
else:
    print(i-1,2**(i-1))
