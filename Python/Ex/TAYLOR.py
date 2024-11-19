import math
n=int(input())
t=0
for i in range(n):
    t+=n**i/math.factorial(i)
print(t)