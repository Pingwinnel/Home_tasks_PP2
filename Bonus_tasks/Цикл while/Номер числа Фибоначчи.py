x=int(input())
x2=1
x1=0
i=1
y=0
if x==1:
    print(1)
    exit(0)
while x!=y:
    if x<y:
     print(-1)
     break
    else:
      y=x2+x1
      x1=x2
      x2=y
      i=i+1
else:
    print(i)
