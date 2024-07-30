def happy(n,res):
    for i in str(n):
        res+=int(i)**2
    return res
n=int(input())
res=0
l=[]
ans=happy(n,res)
l.append(ans)
if ans==1:
    print("Happy")
else:
    if ans not in l:
        ans=happy(ans,res)
    else:
        print("Not Happy")
