class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None
    def append(self,root,n):
        if root is None:
            return node(n)
        if n < root.data:
            root.left=self.append(root.left,n)
        else:
            root.right=self.append(root.right,n)
        return root
    def display(self,d):
        if d:
            self.d(d.left)
            self.d(d.right)
            print(d.data,end=" ")
bst = tree()
print(bst.root)
a=[2,4,1,7,6,3]
for i in a:
    bst.root=bst.append(bst.root,i)
bst.display(bst.root)