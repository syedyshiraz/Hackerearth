ch=str(input())
st=''
for i in ch:
      if(i=='G'):
         st=st+'C'
      elif(i=='C'):
         st=st+'G'
      elif(i=='A'):
         st=st+'U'
      elif(i=='T'):
         st=st+'A'
      else:
          print('Invalid Input')
          st=''
          break
print(st)
   
