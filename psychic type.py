l=int(input())
a=list(map(int,input().split()))
s,e=map(int,input().split())
for i in range(l):
    if(s==e):
        print('Yes')
        flag=1
        break
    elif(a[s-1]==s):
        print('No')
        flag=1
        break
    else:
        s=a[s-1]
        flag=0
if(flag==0):
    print('No')
            
