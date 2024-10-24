def countPairings(n):
    return n if n <= 2 else countPairings(n - 1) + (n - 1) *countPairings(n - 2)

n=int(input())
print(countPairings(n))