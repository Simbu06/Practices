li=list(map(int,input().split()))
n=len(li)
for i in range(0,n-2):
    if(li[i]==li[i+1] and li[i]==[i+2]):
        print(li[i])
    
