n=list(map(int,input().split()))
l=[]
for i in range(len(n)):
    if i%2==0:
        l.append(min(n))
        n.remove(min(n))
    else:
        l.append(max(n))
        n.remove(max(n))
print(l)