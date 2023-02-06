x=int(input())
y=int(input())
d=1
j=1
if x>y:
    d=-1
    j=-1
for i in range(x,y+j,d):
    print(i)
