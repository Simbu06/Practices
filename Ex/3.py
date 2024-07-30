s=input()
st=0
end=len(s)-1
flag=True
while st<end:
    if s[st]!=s[end]:
        flag=False
        break
    st+=1
    end-=1
if flag==True:
    print('Palindrome')
else:
    print('Not')
