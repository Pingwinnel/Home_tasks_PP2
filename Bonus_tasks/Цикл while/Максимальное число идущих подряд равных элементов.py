x=int(input())
c=1
b=0
while x!=0:
    v=int(input())
    x,v=v,x
    if v==x:
        c+=1
    if c>b:
        b=c
    if x!=v:
        c=1
print(b)