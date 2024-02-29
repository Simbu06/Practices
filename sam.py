def rem(pc,pb,bd,pcab):
    tp=pc
    for i in pcab:
        tp+=i
    for i in bd:
        tp-=i
    return tp
    

pc = int(input("Enter Petrol in car:"))
pb=list(map(str,input("Enter Petrol Bunks:").split()))
bd=list(map(int,input("Enter the Bunk Distance:").split()))
pcab=list(map(int,input("Enter the Bunk Capacity:").split()))
ans=rem(pc,pb,bd,pcab)
print("Remaning Petrol is :",ans)