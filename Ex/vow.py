v = ['a','e','i','o','u','A','E','I','O','U']
l = input()
for i in l:
    if i in v:
        print(str(i)*len(l))
        break