def freq(x):
    count=0
    for ch in ar:
        if x==ch:
            count=count+1
    return(count)
l=int(input())
ar=list(input())
ar.sort()
a=freq('a')//2
h=freq('h')//2
e=freq('e')//2
r=freq('r')//2
c=freq('c')
k=freq('k')
t=freq('t')
print(min(h,a,c,k,e,r,t))


