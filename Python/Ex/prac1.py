l=list(map(int,input().split()))
n=[]
for i in range(len(l)):
    m=l[i:i+3]
    if len(m)==3:
        for j in range(len(m)):
            if m[j] < 0:
                n.append(m[j])
                break
            else:
                if j == len(m)-1:
                    n.append(0)
print(n)