class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.front=None
        self.rear = None
    def enqueue(self,data):
        newnode = Node(data)
        if self.front is None and self.rear is None:
            self.front = newnode
            self.rear = self.front
            self.rear.next=self.front
        else:
            self.rear.next = newnode
            self.rear=newnode
            self.rear.next = self.front
    def dequeue(self):
        if self.front is None and self.rear is None:
            print("Underflow!!!")
        else:
            data=self.front.data
            self.front = self.front.next
            self.rear.next = self.front
        return data
    def display(self):
        curr=self.front
        while curr.next is not self.front:
            print(curr.data,id(curr.next))
            curr=curr.next
        print(curr.data, id(curr.next))
        if curr is None:
            print("Queue is Empty....")


obj=queue()
for i in range(int(input())):
    obj.enqueue(int(input()))
c=1
while c!=0 and c<3:
    print("1...Dequeue\n2...Display\n")
    c=int(input("Enter Your Choice : "))
    if c==1:
        print("Dequeued Element is....",obj.dequeue())
    if c==2:
        obj.display()