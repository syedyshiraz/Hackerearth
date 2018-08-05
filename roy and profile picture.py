l=int(input())
n=int(input())
for i in range(n):
   w,h=map(int,input().split())
   if(w<l or h<l and w!=h):
        print('UPLOAD ANOTHER')
   elif(w==l and h==l)or(w==h):
        print('ACCEPTED')
   else:
        print('CROP IT')
