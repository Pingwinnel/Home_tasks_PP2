x=int(input())
x1=int(input())
y=int(input())
y1=int(input())
if (x==y+1 or x==y-1 or y==x+1 or y==x-1 or x==y):
    if (x1==y1+1 or x1==y1-1 or y1==x1+1 or y1==x1-1 or x1==y1):
        print("YES")
    else: 
        print("NO")
else:
    print("NO")
