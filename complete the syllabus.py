def day(x):
    if(x==1):return('MONDAY')
    elif(x==2):return('TUESDAY')
    elif(x==3):return('WEDNESDAY')
    elif(x==4):return('THURSDAY')
    elif(x==5):return('FRIDAY')
    elif(x==6):return('SATURDAY')
    else:return('SUNDAY')
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    add=0
    for i in range(len(a)):
        add=add+a[i]
    if(n%add!=0):
        n=n%add
    temp=0
    count=0
    i=0
    while(n):
        if(i<7):
            ind=i
        else:
            ind=i%7
        count+=1
        
        n=n-a[ind]
        if(temp>=n):
            break
        i+=1
    print(day(count%7))
