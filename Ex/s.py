s=input()
li=['a','e','i','o','u','A','E','I','O','U']
for i in s:
  if i in li:
   ss=i.swapcase()
  else:
    ss=ss+i
print(ss)
