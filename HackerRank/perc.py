student = {}

for i in range(int(input())):
    name, *line = input().split()

    scores = list(map(float, line))

    student[name] = scores

fin = input()

l1 = list(student[fin])

add = sum(l1)

res = add / len(l1)

print('%.2f'%res)