#binary tree
class Node:
    def __init__(self,val):
        self.value=val
        self.rightChild=None
        self.leftChild=None
    def insert(self,data):
        if self.value==data:
            return False
        elif self.value>data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild=Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild=Node(data)
                return True

    def find(self,data):
        if self.value==data:
            return True
        elif self.value>data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))
    def inorder(self):
        if self:
            
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

    def getSize(self):
        if self.leftChild and self.rightChild:
            return 1+self.leftChild.getSize()+self.rightChild.getSize()
        elif self.leftChild:
            return 1+self.leftChild.getSize()
        elif self.rightChild:
            return 1+self.rightChild.getSize()
        else:
            return 1
    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1+max(self.leftChild.getHeight(),self.rightChild.getHeight())
        elif self.leftChild:
            return 1+self.leftChild.getHeight()
        elif self.rightChild:
            return 1+self.rightChild.getHeight()
        else:
            return 1
        
            

class Tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root=Node(data)
            return True
    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def preorder(self):
        print("preorder")
        self.root.preorder()
    def inorder(self):
        print("inorder")
        self.root.inorder()
    def postorder(self):
        print("postorder")
        self.root.postorder()
    def getSize(self):
        if self.root:
            return self.root.getSize()
        else:
            return 0
    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return 0

bst=Tree()
bst.insert(10)
bst.insert(15)
bst.insert(20)
bst.preorder()
bst.postorder()
bst.inorder()
print(bst.getSize())
print(bst.getHeight())
            


    
        
