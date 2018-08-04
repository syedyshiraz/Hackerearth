import math
t=int(input())
for i in range(t):
    index=int(input())
    m=index*(2*index-1)
    l=10**9+7
    print(m%l)
