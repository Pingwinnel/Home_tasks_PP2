i=0
x=int(input())
y=x
while True:
    if x==0:
        print(i)
        break
    elif x>y:
        i=i+1
        y=x
    else:
        y=x
    x=int(input())
