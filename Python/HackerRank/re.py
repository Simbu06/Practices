height=list(map(int,input().split()))
width=1
height=sorted(set(height))
if height[-2]-height[-1]==-1:
    ret=height[-2]*(width+1)
else:
    ret=height[-1]*(width)
print(ret)