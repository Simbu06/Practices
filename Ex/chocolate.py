s=int(input())
l=sorted(list(map(int,input().split())))
m=[]
for i in range(s):
    s=0
    for j in range(i,s+i):
        s+=(l[j+1]-l[j])
    m.append(s)
print(m)