list1=list(map(int, input().split()))
even=[n for n in list1 if n%2==0]
odd=[n for n in list1 if n%2==1]
print(even)
print(odd)
n=len(list1)//2
for i in range(0,n):
    fun=[even[i],odd[i]]
print(fun)
