s=input()
st=0
lt=len(s)-1
s=list(s)
while st < lt:
    s[st],s[lt]=s[lt],s[st]
    st+=1
    lt-=1
for i in s:
    print("".join(i),end="")