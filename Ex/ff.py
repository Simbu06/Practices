list1=[]
n=int(input())
for i in range(n):
    ele=int(input())
    list1.append(ele)
small=0
n=len(list1)
for i in range(0,n):
    if(list1[s]<list1[i]):
        small=list1[s]
        s+=1
    else:
        small=list1[i]
        s+=1
print(small)
        
