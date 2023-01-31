x=int(input())
x1=int(input())
y=int(input())
y1=int(input())
if x==y or x1==y1:
    print("YES")
elif abs(x-y)==abs(x1-y1):
    print("YES")
else:
    print("NO")
