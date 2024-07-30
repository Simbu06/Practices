lis=[]
for i in range(int(input())):
    a = input().split()
    if a[0] == 'append':
        lis.append(int(a[1]))
    elif a[0] == 'insert':
        lis.insert(int(a[1]),int(a[2]))
    elif a[0] == 'remove':
        lis.remove(int(a[1]))
    elif a[0] == 'pop':
        lis.pop()
    elif a[0] == 'reverse':
        lis.reverse()
    elif a[0] == 'sort':
        lis.sort()
    elif a[0] == 'print':
        print(lis)