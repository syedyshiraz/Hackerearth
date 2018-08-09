def palindrome(x):
    y=x[::-1]
    return(x==y)
t=int(input())
for i in range(t):
    p=1
    s=str(input())
    if(palindrome(s)==True):
        print('Palindrome')
    else:
        for j in s:
            p=p*(ord(j)-96)
        print(p)
