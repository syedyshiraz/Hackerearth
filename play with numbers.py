    

n,q=map(int,input().split())
a=list(map(int,input().split()))
for i in range(q):
    l,r=map(int,input().split())
    for j in range(len(a)):
        if(l==a[j]):
            lin=j
        if(r==a[j]):
            rin=j
    s=a[lin+1:rin]
    s.sort()
    print(s.pop(0))


        
    
    
