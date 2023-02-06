y=0
max=0
while True:
    x=int(input())
    if x==0:
        print(y)
        break
    elif x>max:
        y=max
        max=x
    elif x>y:
        y=x
