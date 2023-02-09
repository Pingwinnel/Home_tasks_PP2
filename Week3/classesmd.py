#1task
class String:
    def getString(self):
        g=input()
        self.str=g
    def printString(self):
        print(self.str)
        
#2task
class Shape():
    def area(self):
        self.area=0
        return self.area

class Square(Shape):
    def __init__(self,lenght):
        self.lenght=lenght
        self.width=lenght
    def area(self):
        return self.lenght*self.width
    
#3task
class Rectangle(Shape):
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
    def area(self):
        return self.width*self.lenght

#4task
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def show(self,):
        print(self.x,self.y)
    
    def move(self):
        x1=int(input())
        y1=int(input())
        self.x=x1
        self.y=y1
    
    def dist(self):
        x1=int(input())
        y1=int(input())
        print(self.x+x1,self.y+y1)

x=int(input())
y=int(input())

fir_point=Point(x,y)
fir_point.move()
fir_point.show()
fir_point.dist()

#5task
class Bank():
    def __init__(self,bal,owner) -> None:
        self.own=owner
        self.balance=bal
    def deposit(self):
        x=int(input())
        self.balance=self.balance+x
    def with_draw(self):
        x=int(input())
        if x>self.balance:
            print("You don't have enough money")
        else:
            self.balance=self.balance-x

#6task 
def prime_find(n):
    for i in range(2,n,1):
        if n%i==0:
         return False
    return True
nums=input().split()

prime_nums=list(filter(lambda x:prime_find(int(x)),nums))
print(prime_nums)
        
        