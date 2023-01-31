x=int(input())
y=int(input())
x1=int(input())
y1=int(input())
ox = x -x1 
oy = y - y1
step_x = bool((abs(ox) == 2))
step_y = bool((abs(oy) == 2))
side_x = bool((abs(ox) == 1))
side_y = bool((abs(oy) == 1))
if ((step_x and side_y) or (step_y and side_x)):
        print("YES")
    
else :
      print("NO")
