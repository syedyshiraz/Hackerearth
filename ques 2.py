n,x,y=map(int,input().split())
li=list(map(int,input().split()))
a=max(li)
b=min(li)
if(b>=x and a<=y):
    print('YES')
else:
    print('NO')
