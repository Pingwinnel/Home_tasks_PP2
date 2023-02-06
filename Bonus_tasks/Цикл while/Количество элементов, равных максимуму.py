i=0
max=0
y=0
lst=[]
z=0
while True:
    x=int(input())
    lst.append(x)
    if x==0:
        break
    elif x>max:
        max=x
while len(lst)>z:
    if max==lst[z]:
        y=y+1
        z=z+1
    else:
        z=z+1
else:
    print(y)
