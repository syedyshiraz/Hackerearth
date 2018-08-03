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
def near(x):
    st=[]
    sp=[]
    for i in range(x-60,x):
        if(isprime(i)==True):
            st.append(i)
    st.sort()
    r=max(st)
    for j in range(x,x+60):
        if(isprime(j)==True):
            sp.append(j)

    sp.sort()
    q=min(sp)
    p=abs(x-r)
    z=abs(q-x)
    if(p>z):
        return(min(sp))
    elif(p<=z):
        return(max(st))
        
t=int(input())
for i in range(t):
    num=int(input())
    print(near(num))
