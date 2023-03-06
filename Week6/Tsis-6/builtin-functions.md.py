
#1ex
def Sum_list(lis):
    lis_sum=sum(lis)
    return lis_sum

#2ex
def count_upper_lowwer(str):
    upp=0
    low=0
    for ch in str:
        if ch.isupper():
            upp+=1
        elif ch.islower():
            low+=1
    return f"Upper_case: {upp} \nLower_case: {low}"

#3ex
def Palidrome_test(str):
    rev_str="".join(reversed(str))
    if str==rev_str:
        print("Palindrome")
    else:
        print("No palindrome")
#4ex
import time as t
import math

def Sqrt_after_time(num,time):
    t.sleep(time/1000)
    return math.sqrt(num)

#5ex
def True_test(tuple):
    if all(tuple)==True:
        return True
    else:
        return False

