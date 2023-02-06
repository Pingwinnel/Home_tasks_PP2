x=int(input())
sum=1
sum2=0
for i in range(x+1):
    if i==0:
        sum=1
    else:
        sum=sum*i
        sum2=sum2+sum
        
print(sum2)
