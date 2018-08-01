import math
def nextseat(num):
    if math.ceil(n/6)%2==0:
        return subtract(num)
    else:
        return add(num)
def add(x):
    m=x%6
    if m==0:
        return x+1
    elif m==1:
        return x+11
    elif m==2:
        return x+9
    elif m==3:
        return x+7
    elif m==4:
        return x+5
    elif m==5:
        return x+3
def subtract(y):
    l=y%6
    if l==0:
        return y-11
    elif l==1:
        return y-1
    elif l==2:
        return y-3
    elif l==3:
        return y-5
    elif l==4:
        return y-7
    else:
        return y-9
def seattype(n):
    if (n%6==0 or n%6==1):
        return('WS')
    elif(n%6==2 or n%6==5):
        return('MS')
    else:
        return('AS')
t=int(input())
for i in range(t):
    n=int(input())
    print(nextseat(n),end=' ')
    print(seattype(n))

    
