class Node(object):
    def  __init__(self,data,next_node=None):
        self.data=data
        self.next_node=next_node
    def get_next(self):
        return self.next_node
    def set_next(self,next_node):
        self.next_node=next_node
    def get_data(self):
        return self.data
    def set_data(self,data):
        self.data=data
    def has_next(self):
        if self.get_next() is None:
            return False
        return True
    def toString(self):
        return str(self.get_data())

class LinkedList(object):
    def __init__(self,r=None):
        self.root=r
        self.size=0
    def get_size(self):
        return self.size
    def add(self,d):#add at beginning
        new_node=Node(d,self.root)
        self.root=new_node
        self.size+=1
    def remove(self,data):
        this_node=self.root
        prev_node=None
        while this_node is not None:
            if this_node.get_data() == data:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root=this_node.get_next()
                self.size-=1
                return True
            else:
                prev_node=this_node
                this_node=this_node.get_next()
        return False
    def find(self,data):
        this_node=self.root
        while this_node is not None:
            if this_node.get_data() == data:
                return True
            this_node=this_node.get_next()
        return False
    def print_list(self):
        this_node=self.root
        while this_node.has_next():
            print(this_node.toString())
            this_node=this_node.get_next()

myList=LinkedList()
myList.add(1)
myList.add(4)
myList.add(6)
myList.add(2)
print("size:",myList.get_size())
'''myList.remove(6)
print("size:",myList.get_size())
print("Is 2 present?",myList.find(-2))'''
myList.print_list()
        
        
        
        
