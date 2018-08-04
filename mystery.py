t=int(input())
for i in range(t):
    n=int(input())
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    print(count)
        
