def sort(a):
    for j in range(len(a)):
        for i in range(0,len(a)-1):
            if(a[i]>a[i+1]):
                a[i+1],a[i]=a[i],a[i+1]
a=list(map(int,input().split()))
sort(a)
print(a)
