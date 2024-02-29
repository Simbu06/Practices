st=[]
st1=[]
for i in range(int(input())):
    name=input()
    score=float(input())
    st.append([name,score])

st.sort(key=lambda x:x[1])
min=st[0][1]
smin=None
for i in st:
    if i[1] > min:
        smin=i[1]
        break
for i in st:
    if i[1] == smin:
        st1.append(i[0])
for i in sorted(st1):
    print(st1)