def sort(a):
    for i in range(0,len(a)-1):
        val=i
        for j in range(i+1,len(a)):
            if a[val]>a[j]:
                val=j
            a[i],a[val]=a[val],a[i]
a=list(map(int,input().split()))
print(a)
sort(a)
print(a)
