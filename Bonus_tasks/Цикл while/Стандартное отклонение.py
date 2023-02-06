i=0
sum=0
j=0
lst=[]
sum2=0
while True:
    x=int(input())
    if x==0:
     arfmetic=sum/i
     break
    else:
        sum=sum+x
        i=i+1
        lst.append(x)
for j in lst:
    sum2=(sum2)+(j-arfmetic)**2
print((sum2/int(i-1))**(0.5))
