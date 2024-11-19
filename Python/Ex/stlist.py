class stack:
    def __int__(self):
        self.data=[]
    def empty(self):
        return len(self.data)==0
    def push(self,a):
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
def per(c):
    if c == "^":
        return 3
    elif c == "*" or c == "/":
        return 2
    elif c == "+" or c == "-":
        return 1
    else:
        return 0
def op(c):
    return ((ord(c)>=ord('a') and ord(c)<=ord('z'))or(ord(c)>=ord('A') and ord(c)<=ord('Z'))or(ord(c)>=ord('0') or ord(c)<=ord('9')))
def itp(s,stack):
    pf=[]
    for i in range(len(s)):
        if op(s[i]):
            pf.append(s[i])
        elif s[i] == '(':
            stack.push(s[i])
        elif s[i]==')':
            while stack.peek()!='(':
                pf.append(stack.pop())
            stack.pop()
        else:
            while(not stack.empty()) and (per(s[i])<=per(stack.peek())):
                pf.append(stack.pop())
                stack.push(s[i])
            while not stack.empty():
                pf.append(stack.pop())
            return ''.join(pf)

s=input()
stack=stack()
post=itp(s,stack)
print(post)