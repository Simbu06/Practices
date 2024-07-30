bl=[]
ns=4
nf=list(map(int,input().split()))
for i in range(ns):
    b=sum(int(d) for d in str(nf[i]))
    bl.append(b)
print(bl)
