n=int(input())
fp=[0 for i in range(n+1)]
for i in range(n+1):
    if i <= 2:
        fp[i]=i
    else:
        fp[i]=fp[i-1] + (i-1) * fp[i-2]
print(fp[n])