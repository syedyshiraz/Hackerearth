n=int(input())
for i in range(n+1,n+12):
    if('3' not in str(i) and i%3!=0):
        print(i)
        break
