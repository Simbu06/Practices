# Perfect Square and Perfect cube
# num=list(map(int,input().split()))
# for j in num:
#     for i in range(1,j):
#         if i*i == j:
#             print(f"{i*i}'s Perfect Square is {i}")
#             break
#
#         elif i*i > j:
#             print(f"{i} is Not Have Perfect Square")
#             break

# Fibonacci Series
# n=int(input())
# f=[0,1]
# for i in range(n-2):
#     f.append(f[i]+f[i+1])
# print(f)

# LCM of 2 Numbers
# n1=int(input())
# n2=int(input())
# i=1
# while n1*i != n2*i:
#     i+=1
# print(n1*i)

# Linear Search
# n=int(input())
# l=list(map(int,input().split()))
# f=0
# for i in l:
#     if n == i:
#         f=1
#         print(l.index(i)+1)
#         break
# if f==0:
#     print("no")

# Bubble sort
# def sort(a):
#     for j in range(len(a)):
#         for i in range(0,len(a)-1):
#             if(a[i]>a[i+1]):
#                 a[i+1],a[i]=a[i],a[i+1]
# a=list(map(int,input().split()))
# sort(a)
# print(a)

# Palindrome
# s=input()
# st=0
# lt=len(s)-1
# s=list(s)
# while st < lt:
#     s[st],s[lt]=s[lt],s[st]
#     st+=1
#     lt-=1
# for i in s:
#     print("".join(i),end="")