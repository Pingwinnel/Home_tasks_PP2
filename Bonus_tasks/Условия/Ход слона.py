x=int(input())
x1=int(input())
y=int(input())
y1=int(input())
if x==y:
    print("NO")
else:
    if x-y==x1-y1 or x-y==-(x1-y1):
        print("YES")
    else:
        print("NO")
