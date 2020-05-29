from itertools import combinations
l=combinations('001',2)
s=set()
for i in l:
	s1=''.join(list(i))
	s.add(s1)
l=list(map(int,list(s)))
l.sort()
print(l[-1])