l,q=map(int,input().split())
a=list(map(int,input().split()))
for i in range(q):
    o,x,y=map(int,input().split())
    if(o==1):
        a[x]=y
    else:
        sum=0
        for i in range(x,y+1):
            sum=sum+a[i]
        print(sum)
            
        
