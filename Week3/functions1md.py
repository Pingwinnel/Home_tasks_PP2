
#1 task
def convert_grams (gr):
    return gr*28.3495231

#2 task
def Faren_to_cel(Fahren):
    return (5 / 9) *( Fahren-32)

#3 task
def Count_legsheads(legs , head):
    rabhead=(legs-head*2)/2
    chichead=head-rabhead
    return (int(rabhead),int(chichead))


#4task
def filter_prime(list):
    i=0
    while i<len(list):
        if list[i]>1:
            for j in range(2,int(list[i]/2)+1):
                if(list[i] % j) == 0:
                    list.pop(i)
                    i=i-1
                    break
        else:
            list.pop(i)
            i=i-1
        i+=1


#5task
from itertools import permutations
str=input()
perms = [''.join(p) for p in permutations(str)]
print(perms)
        
#6task                
def reverse_word(g):
    r=g.split(' ')
    r.reverse()
    for i in r:
        print(i,end=' ')        



#7task
def has33 (lis):
    p=False
    for i in range(len(lis)-1):
        if lis[i]==3 and lis[i+1]==3 :
            p=True
            break
        else:
            pass
    if p==True:
        print(p)
    else:
        print(p)


#8task
def has_007(lis):
    h=0
    j=0
    p=False
    for i in range(len(lis)):
        if j>=2:
            h=7
            if lis[i]==h:
                p=True
                break
        elif lis[i]==h and j<2:
            j=j+1
    print(p)

#9task
def sphere_vol(rad):
    print(4/3*3.14*rad**3)

#10task
def uique_elem(lis):
    r=[]
    for i in range(len(lis)):
        for j in range(len(lis)):
            if i==j:
                continue
            elif lis[i]==lis[j]:
                lis[j]=" "
    
    for i in lis:
        if i!=' ':
              r.append(i)   
    print(r)     
    
#11task
def palindrome(word):
    print(word==word[::-1])


#12task
def histogram(lis):
    for i in lis:
        for j in range(i):
            print('*',end='')
        print()


import random        
#13TASK
def Guess_num():
    p=False
    rand_num=random.randrange(1,20)
    i=0
    gues="Take a guess."
    low="Your guess is too low."
    more="Your guess is too more."
    print('Hello! What is your name?')
    name=input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    print(gues)
    
    while p!=True:
        num=int(input())
        if num==rand_num:
            p=True
            i=i+1
            print(f"Good job, {name}! You guessed my number in {i} guesses!")
        elif num>rand_num:
            print(more,f'\n {gues}')
            i=i+1
        else:
            print(low,f'\n{gues}')
            i=i+1


    
    
    