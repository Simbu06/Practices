class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            newnode=Node(data)
            self.tail.next=newnode
            self.tail=newnode
    def insertend(self,data):
        newnode=Node(data)
        self.tail.next=newnode
        self.tail=newnode
    def display(self):
        temp=self.head
        while temp is not None:
            print(id(temp),temp.data,id(temp.next))
            temp=temp.next
obj=Sll()
for i in range(int(input())):
    obj.create(int(input()))
obj.display()
obj.insertend(int(input()))
obj.display()