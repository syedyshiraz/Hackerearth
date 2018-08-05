l,r,k=map(int,input().split())
num=0
for i in range(l,r+1):
    if(i%k==0):
        num += 1
print(num)
    
