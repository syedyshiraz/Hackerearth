t=int(input())
for i in range(t):
    n=int(input())
    su=0
    for j in range(1,n//2+1):
        if(n%j==0):
            su=su+j
            
    print(su)   
