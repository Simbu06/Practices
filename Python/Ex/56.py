class Stack:
    def _init_(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
def is_balanced(expression):
    stack=Stack()
    open="[({"
    close="])}"
    for char in expression:
        if char in open:
            stack.push(char)
        elif char in close:
            if stack.is_empty():
                return False
            top=stack.pop()
            if open.index(top)!=close.index(char):
                return False
    return stack.is_empty()
expression="[({})]"
print(is_balanced(expression))
expression="{[()]]"
print(is_balanced(expression))