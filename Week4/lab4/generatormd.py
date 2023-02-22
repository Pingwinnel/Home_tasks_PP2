#1ex
def pow_2(n):
    yield n*n
#2ex
def even():
    n=int(input())
    even_num=(i for i in range(n+1) if i%2==0)
    for j in even_num:
        print(j)
#3ex
def divede_3_4(n):
    div=(i for i in range(n+1) if i%3==0 and i%4==0)
    for i in div:
        yield i
#4ex
def sque(a,b):
    for i in range(a,b+1):
        yield i*i
#5ex
def down_to_zero(n):
    for i in range(n,0,-1):
        yield i
down=down_to_zero(5)

for j in range(0,5):
    print(next(down))