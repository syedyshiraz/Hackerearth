n=str(input())
for ch in n:
    if(str.isupper(ch)==True):
        print(str.lower(ch),end='')
    else:
        print(str.upper(ch),end='')

