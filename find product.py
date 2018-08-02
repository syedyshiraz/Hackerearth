n=int(input())
answer=1
s=list(map(int,input().split()))
for j in range(len(s)):
    answer=(answer*int(s[j]))%(10**9+7)
print(answer)
    
