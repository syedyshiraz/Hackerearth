def day(x):
    if x==0:return('MONDAY')
    elif x==1:return('TUESDAY')
    elif x==2:return('WEDNESDAY')
    elif x==3:return('THURSDAY')
    elif x==4:return('FRIDAY')
    elif x==5:return('SATURDAY')
    else: return('SUNDAY')
t=int(input())
for i in range(t):
    k=int(input())
    sub=list(map(int,input().split()))
    count=0
    i=0
    while((i%7)>-1):
        count =i%7
        if(k<=sub[i%7]):
            print(day(count))
            break
        else:
            k=k-int(sub[i%7])
            i +=1
         
        
        
        
        
