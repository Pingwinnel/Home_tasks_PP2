x=int(input())
y=int(input())
z=int(input())
if x>y and x>z:
    if y>z:
        print(z)
    else:
        print(y)
elif y>x and y>z:
    if x>z:
        print(z)
    else:
        print(x)
else:
    if x>y:
        print(y)
    else:
        print(x)
