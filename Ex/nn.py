list1=[]
n=int(input())
k=n-1
for i in range(n):
    ele=int(input())
    list1.append(ele)
list1.sort()
m=n//2
for i in range(m):
    print(list1[k],end=" ")
    print(list1[i],end=" ")
    k-=1
