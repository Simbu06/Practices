lis=[]
lis1=[]
for i in range(int(input())):
    s=input().split()
    lis.append(s)
n=input()
a=None
for k in range(0,len(lis)):
    if a==1:
        break
    for i in range(1,len(lis)+2):
        if n == lis[k][0]:
            if len(lis1) != 3:
                lis1.append(lis[k][i])
            else:
                a=1
lis1=list(map(float,lis1))
ans=sum(lis1,0)/(len(lis1))
print("{:.2f}".format(ans))