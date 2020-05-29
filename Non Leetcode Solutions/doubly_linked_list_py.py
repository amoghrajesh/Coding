class Node(object):
    def  __init__(self,data,next_node=None,prev_node=None):
        self.data=data
        self.next_node=next_node
        self.prev_node=prev_node
    def get_next(self):
        return self.next_node
    def set_next(self,next_node):
        self.next_node=next_node
    def get_prev(self):
        return self.prev_node
    def set_next(self,prev_node):
        self.prev_node=prev_node
    def get_data(self):
        return self.data
    def set_data(self,data):
        self.data=data

class LinkedList(object):
    def __init__(self,r=None):
        self.root=r
        self.size=0
    def get_size(self):
        return self.size
    def add(self,d):#add at beginning
        new_node=Node(d,self.root)
        if self.root:
            self.root.set_prev(new_node)
        self.root=new_node
        self.size+=1
    def remove(self,data):
        this_node=self.root
        while this_node:
            if this_node.get_data() == data:
                next=this_node.get_next()
                prev=this_node.get_prev()
                if next:
                    next.set_prev(prev)
                if prev:
                    prev.set_next(next)
                else:
                    self.root=this_node
                self.size-=1
                return True
        else:
            this_node=this_node.get_next()
    return False
                
            
        




        
    def find(self,data):
        this_node=self.root
        while this_node is not None:
            if this_node.get_data() == data:
                return True
            this_node=this_node.get_next()
        return False

myList=LinkedList()
myList.add(1)
myList.add(4)
myList.add(6)
myList.add(2)
print("size:",myList.get_size())
myList.remove(6)
print("size:",myList.get_size())
print("Is 2 present?",myList.find(-2))
        
        
        
        
