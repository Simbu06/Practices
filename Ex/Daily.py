# Armstrong
# s=int(input())
# l=0
# for i in str(s):
#     l+=int(i)**len(str(s))
# if l!=s:
#     print("Not Armstrong")
# print("Armstrong")

# Adam
# def rev(a):
#     a=list(a)
#     st=0
#     ed=len(a)-1
#     while st<ed:
#         a[st],a[ed]=a[ed],a[st]
#         st+=1
#         ed-=1
#     return ''.join(a)
# n=int(input())
# s1=n*n
# f1=rev(str(n))
# s2=int(f1)*int(f1)
# f2=rev(str(s2))
# if s1!=int(f2):
#     print("Not Adam")
# else:
#     print("Adam")

# 2D List
n=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
print(mat)
sum1=0
for i in range(n):
        sum1+=mat[i][i]
print(sum1)

#