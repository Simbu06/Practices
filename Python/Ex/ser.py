l=[]
odd,even=0,0
n=int(input())
for i in range(n):
    if len(l) == 0:
        l.append(odd),l.append(even)
    elif i%2 == 0:
        even+=6
        l.append(even)
    else:
        odd+=7
        l.append(odd)
print(l)