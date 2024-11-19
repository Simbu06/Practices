def rotate(mat):
    n = len(mat)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = mat[i][j]
    for l in rotated:
        print(*l)

n=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
rotate(mat)
