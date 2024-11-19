def odd(a):
    mul=m*a
    return mul

n=input()
m=1
for i in range(1,n+1):
    if(i%2==1):
        odd(i)
print(odd(m))
