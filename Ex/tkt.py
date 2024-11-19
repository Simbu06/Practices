l = int(input())
n = (l-1) // 2
s = [1] * (n+1)
for i in range(1,n+1):
    j = i
    while i + j + 2 * i * j <= n:
        s[i + j + 2 * i * j] = 0
        j += 1
# print(s)
primes = [2] if l > 2 else []
primes.extend([2 * i + 1 for i in range(1, n + 1) if s[i]])
print(primes)