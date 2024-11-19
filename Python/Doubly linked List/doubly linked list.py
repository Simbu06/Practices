class node:
    def _init_(self,data):
        self.data = data
        self.next = self.prev = None


class dll:
    def __init__(self):
        self.head = self.tail = None

    def _init_(self):
        self.head = self.tail = None

    def create(self,data):
        if self.head is None:
            self.head = node(data)
            self.tail = self.head
        else:
            newnode = node(data)
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def sorted(self):
        temp = self.head.next
        temp1 = self.head
        while temp1 != self.tail:
            if temp is not None:
                if temp1.data < temp.data:
                    temp1.data, temp.data = temp.data, temp1.data
                    temp = temp.next
                else:
                    temp = temp.next
            else:
                temp1 = temp1.next
                temp = temp1.next

    def display(self):
        temp = self.head
        while temp is not None:
            # print(id(temp), id(temp.prev), temp.data, id(temp.next))
            print(temp.data)
            temp = temp.next

obj = dll()
for i in range(int(input())):
    obj.create(int(input()))
obj.sorted()
obj.display()