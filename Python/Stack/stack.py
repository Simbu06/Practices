class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class st:
    def __init__(self):
        self.top=None
    def push(self,data):
            newnode=Node(data)
            newnode.next=self.top
            self.top=newnode
    def pop(self):
        if self.top is None:
            print("Underflow!!!")
        else:
            data=self.top.data
            self.top = self.top.next
            return data
  def peek(self):
        if self.top is None:
            print("Underflow!!!")
        return self.top.data
    def display(self):
        curr=self.top
        if self.top:
            while curr:
                print(curr.data,end=" ")
                curr=curr.next
            print()
        else:
            print("Stack Is Empty.....")


obj=st()
for i in range(int(input())):
    obj.push(int(input()))
c=1
while c!=0 and c<4:
    print("1...Pop\n2...Peek\n3...Display\n")
    c=int(input("Enter Your Choice : "))
    if c==1:
        print("Poped Element is....",obj.pop())
    if c==2:
        print("Peek Element is....", obj.peek())
    if c==3:
        obj.display()
