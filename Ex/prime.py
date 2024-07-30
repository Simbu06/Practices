num=int(input())
flag=0
if num>1:
    for i in range(2,(num//2)+1):
        if num % i == 0:
            flag=0
            break
        else:
            flag=1
if flag==1:
    print("Prime")
else:
    print("Not Prime")