n=int(input())
c=0
a=[]
for i in range (n):
    ele=int(input())
    a.append(ele)
print(n-a.count(a[0]))
