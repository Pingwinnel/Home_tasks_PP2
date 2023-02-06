x=input()
y=x.find('h')
z=x.rfind('h')
print(x[:y+1]+x[y+1:z].replace('h','H')+x[z:])
