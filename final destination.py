s=input()
x=0
y=0
for i in s:
    if(i=='L'):
        x-=1
    elif(i=='R'):
        x+=1
    elif(i=='U'):
        y+=1
    elif(i=='D'):
        y-=1
print(x,y)
