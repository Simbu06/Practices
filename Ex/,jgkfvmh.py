class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class dequeue:
    def __init__(self):
        self.front=None
        self.dequeuesize=0
    def insertbeg(self,data):
        if self.front==None:
            self.front=node(data)
            self.dequeuesize=self.dequeuesize+1
        else:
            newnode=node(data)
            self.front.next=newnode
            self.front=newnode
            self.dequeuesize=self.dequeuesize+1
    def insertaft(self,data):
        if self.front==None:
            self.front=node(data)
            self.dequeuesize=self.dequeuesize+1
        else:
            newnode=node(data)
            self.front.next=newnode
            self.front=newnode
            self.dequeuesize=self.dequeusize+1
    def delbeg(self):
        self.front=self.front.next
        self.dequeuesize=self.dequeuesize-1
    def delaft(self):
        temp=self.front
        prev=None
        while temp.next !=None:
            prev=temp
            prev.next=temp.next
            self.dequeuesize=self.dequeuesize-1
    def getfront(self):
        if self.front is None:
            return-1
        return(self.front.data)
    def getrear(self):
        if self.front is None:
            return -1
        return(self.front.data)
obj=dequeue()
n=int(input())
for i in range(n):
    ele=int(input())
    obj.insertbeg(ele)
obj.delbeg()
obj.getfront()
    
