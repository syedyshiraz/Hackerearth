t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(b%a==0):
        print('Yes')
    else:
        print('No')
