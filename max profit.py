t=int(input())
a=list(map(int,input().split()))
pro=0
for i in range(t):
    if(a[i]==max(a)):
        index=i+1
        a=a[:index]
        break
a.sort()
print(a[index-1]-a[0])
