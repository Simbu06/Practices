class Stack:
    def __init__(self):
        self.data = []
    def empty(self):
        return len(self.data) == 0
    def push(self, a):
        self.data.append(a)
    def pop(self):
        if not self.empty():
            return self.data.pop()
        else:
            return None
    def peek(self):
        if not self.empty():
            return self.data[-1]
        else:
            return None

def precedence(c):
    if c == "^":
        return 3
    elif c == "*" or c == "/":
        return 2
    elif c == "+" or c == "-":
        return 1
    else:
        return 0

def is_operand(c):
    return ((ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('0') and ord(c) <= ord('9')))

def infix_to_postfix(s, stack):
    postfix = []
    for i in range(len(s)):
        if is_operand(s[i]):
            postfix.append(s[i])
        elif s[i] == '(':
            stack.push(s[i])
        elif s[i] == ')':
            while stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while (not stack.empty()) and (precedence(s[i]) <= precedence(stack.peek())):
                postfix.append(stack.pop())
            stack.push(s[i])
    while not stack.empty():
        postfix.append(stack.pop())
    return ''.join(postfix)

s = input("Enter the infix expression: ")
stack = Stack()
postfix = infix_to_postfix(s, stack)
print("The postfix expression is: ", postfix)
