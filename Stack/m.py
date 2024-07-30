class Node:
    def __int__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dll:
    def __int__(self):
        self.head=None
        self.tail=None
    def create(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            newnode = Node(data)
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
    def rem(self,n):
        temp=self.head
        for i in range(n+1):
            temp=temp.next
        self.head=temp

    def display(self):
        temp=self.head
        while temp.next is not None:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data)

obj=dll()
l=list(map(int,input().split()))
n= int(input())
for i in range(len(l)):
    obj.create(l[i])
obj.rem(n)
obj.display()