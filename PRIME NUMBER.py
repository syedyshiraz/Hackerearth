import math
def isprime(n):
    m=2
    while True:
        if(n==2 or n==3):
            m=1
            break
        elif(n==1):
            m=0
        else:
            m=1
            for i in range(2,n//2+1):
                if(n%i==0):
                    m=0
                    break
            
        break
                
    return(m==1)
num=int(input(''))
for j in range(1,num):
    if(isprime(j)==True):
        print(j,end=' ')
  
                           
