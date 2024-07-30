n=list(map(int,input().split()))
gcd=[]
gcd1=[]
for i in n:
    for j in range(1,(i//2)+1):
        if i%j == 0 and j not in gcd:
            gcd.append(j)
        elif i%j == 0 and j in gcd:
            gcd1.append(j)
if len(gcd)>len(gcd1):
    print(gcd1[-1])
else:
    print(gcd[-1])