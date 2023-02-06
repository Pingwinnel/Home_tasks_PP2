i=0
sum=0
while True:
    x=int(input())
    if x==0:
        print(sum/i)
        break
    else:
        sum=sum+x
        i=i+1
