def fib(list1):
    sum=0
    for i in range(0,n):
        sum+=list1[i]
    return sum

list1=[]
n=int(input())
for i in range(n):
    list1.append(int(input()))
sum=fib(list1)
print(sum)