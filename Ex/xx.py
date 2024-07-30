class index:
    def __init__(self,a):
        self.a=a
    def val(self):
        for i in range(len(self.a)):
            a=self.a[i]
            print(i,a)
        
        
    
a=list(map(int,input().split()))
obj=index(a)
obj.val()


            
