def rev(a):
    val=0
    while(a!=0):
        rem=a%10
        val=val*10+rem
        a//=10
        return val
    
def adam(f):
    

f=int(input())
f1=f*f
first=rev(f)
f2=first*first
sec=rev(f2)
if(f1==sec):
    print("ADAM")
else:
    print("NOT")