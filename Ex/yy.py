list1=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
count=1
alice=list1[1]
for i in range(0,n):
    if(alice==list1[i]):
        count+=1

print(count)
