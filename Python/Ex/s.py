# n = int(input())
# arr = list(map(int,input().split()))
# tar = int(input())
# k = []
# i = 0
# while i < n:
#     if sum(k) < tar:
#         k.append(arr[i])
#         i += 1
#     elif sum(k) == tar:
#         break
#     else:
#         k.pop(0)
# # print(k)
# print([arr.index(k[0])+1,arr.index(k[-1])+1])

# next

import string
l = list(string.ascii_uppercase)
k = input()
ans = 0
for i in range(len(k)):
    ans += (l.index(k[i])+1) * (len(l)**(len(k)-(i+1)))
print(ans)