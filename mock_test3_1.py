import queue 
class node: 
	def __init__(self, val, level): 
		self.val = val 
		self.level = level 
def minOperations(x, y): 
	visit = set() 
	q = queue.Queue() 
	n = node(x, 0) 
	q.put(n) 
    
    
	while (not q.empty()): 
		t = q.get() 
		if (t.val == y): 
			return t.level
		visit.add(t.val) 
		if(int(str(t.val)[::-1]) ==y or t.val//10 ==y):
			return t.level+1
        
		if (int(str(t.val)[::-1]) not in visit): 
			n.val = int(str(t.val)[::-1])
			n.level = t.level + 1
			q.put(n)  
		if (t.val//10 >= 0 and t.val//10 not in visit): 
			n.val = t.val//10
			n.level = t.level + 1
			q.put(n)
	return -1

if __name__ == '__main__': 

	x = 100
	y = 100
	print(minOperations(x, y)) 