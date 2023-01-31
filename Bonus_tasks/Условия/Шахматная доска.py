x=int(input())
x1=int(input())
y=int(input())
y1=int(input())
if (x%2==0 and y%2==0) or (x%2==1 and y%2==1) :
    if x1%2==0 and y1%2==0:
        print("YES")
    elif x1%2==1 and y1%2==1 :
       print("YES")
    else :
        print("NO")
elif x1%2!=y1%2:
    print("YES")
else:
    print("NO")
