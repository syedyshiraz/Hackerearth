n=int(input())
x,y,p=map(int,input().split())
a=[]
for i in range(n):
    a.append([])
    for j in range(n):
        dist=max(abs(x-i),abs(y-j))
        if(dist>=p):
            a[i].append(0)
        else:
            a[i].append(p-dist)
for l in a:
    print(*l,sep=" ")
            
