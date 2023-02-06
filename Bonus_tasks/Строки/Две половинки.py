x=input()
if len(x)%2==0:
    y=len(x)/2
    y=int(y)
    str1=x[:y]
    str2=x[y:]
    print(str2+str1)
else:
    y=len(x)/2
    y=int(y)
    str1=x[:y+1]
    str2=x[y+1:]
    print(str2+str1)
