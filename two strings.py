t=int(input())
for i in range(t):
    a,b=list(map(list,input().split()))
    a.sort()
    b.sort()
    if(a==b):
        print('YES')
    else:
        print('NO')
    
