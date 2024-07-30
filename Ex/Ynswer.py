s=list(map(str,input().split()))
st=list(map(str,input().split()))
en=list(map(str,input().split()))
count=0
for i in s:
    if(st[0]==s[i]):
        continue
        if(en[0]==s[i]):
            break
        else:
            count+=1
print(count)
        
