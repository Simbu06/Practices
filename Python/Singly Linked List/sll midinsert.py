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
    def midinsert(self,data,pos):
        temp=self.head
        c=0
        while c<pos-1:
            temp=temp.next
            c+=1
        newnode=Node(data)
        newnode.next=temp.next
        temp.next=newnode
    def display(self):
        temp=self.head
        while temp is not None:
            print(id(temp),temp.data,id(temp.next))
            temp=temp.next
obj=Sll()
for i in range(int(input())):
    obj.create(int(input()))
obj.display()
pos=int(input("Enter the Position:"))
obj.midinsert(int(input()),pos)
obj.display()