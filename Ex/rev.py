def check(a):
    for i in range(0,len(a)):
        if((pas[i]>='a' and pas[i]<='z')or(pas[i]>='0' and pas[i]<='9')):
            return 1
        else:
            return 0
pas=input()
sp=['@','#','$','&','%']
if(len(pas)>=8):
    for i in range(0,len(pas)):
        if(pas[i]>='A' and pas[i]<='Z'):
            True
            b=check(pas)
            if(b==1):
                if pas in sp:
                    print("Strong")
                else:
                    print("Fuck")
        else:
            print("Fuck")
else:
    print("Not Enough")
            
