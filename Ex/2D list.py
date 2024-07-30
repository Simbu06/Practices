#/// 2D List Creation
# r=int(input())
# c=int(input())
# mat=[]
# mul=1
# for i in range(r):
#     a=[]
#     for j in range(c):
#         a.append(int(input()))
#     mat.append(a)
# #//Diagonal Multiplication
# for i in range(r):
#     for j in range(c):
#         if i==j:
#             mul*=mat[i][j]
# print(mul)
# print(mat)
#//Matrix Multiplication
# n=int(input())
# mat1=[]
# mat2=[]
# mul=[[0,0],[0,0]]
# for i in range(n):
#     a=[]
#     for j in range(n):
#         a.append(int(input()))
#     mat1.append(a)
# for i in range(n):
#     b=[]
#     for j in range(n):
#         b.append(int(input()))
#     mat2.append(b)
# for i in range(len(mat1)):
#     for j in range(len(mat2)):
#         for k in range(n):
#             mul[i][j]+=mat1[i][k]*mat2[k][j]
# print(mul)


