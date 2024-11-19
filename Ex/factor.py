def factor(a):
    f=[a]
    k=a//2
    while k >= 10:
        if a%k == 0:
            f.append(k)
            k//=2
        else:
            break
    for i in range(1,f[-1]):
        if a % i == 0:
            f.append(i)
    return sorted(f)
l=list(map(int,input().split()))
for i in l:
    print(factor(i))
# def fact(n):
#     for i in range(1,n+1):
#         if(n%i==0):
#             print(i)
# a=list(map(int,input().split()))
# n=len(a)
# for i in range(0,n):
#     fact(a[i])
