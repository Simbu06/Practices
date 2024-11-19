def sort(a):
    for i in range(1,len(a)):
        temp=a[i]
        j=i-1
        while j>=0 and temp<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp
a=list(map(int,input().split()))
print(a)
sort(a)
print(a)
