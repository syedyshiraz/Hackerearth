t=int(input())
for i in range(t):
    n=int(input())-1
    m=n//3
    p=n//5
    q=n//15
    s3=(3*(m**2+m))//2
    s5=(5*(p**2+p))//2
    s15=(15*(q**2+q))//2
    print(s3+s5-s15)
