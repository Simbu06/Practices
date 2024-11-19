n=int(input())
p=[]
for i in range(2,n+1):
     l=0
     for j in range(2,(i//2)+1):
          if i % j == 0:
               l=1
               break
     if l==0:
          p.append(i)
print(p)
