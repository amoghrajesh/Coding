s=input()
t=input()
maxCost=int(input())
n=len(s)
maxlength=0
i=0
start=0
while i<n:
	if maxCost-abs(ord(s[i])-ord(t[i]))>=0:
		#include this one in the length
		maxCost-=abs(ord(s[i])-ord(t[i]))
		i+=1
		
	else:
		#slide the start by a position using start
		maxlength=max(maxlength,i-start)
		maxCost+=abs(ord(s[start])-ord(t[start]))
		start+=1
		
print(maxlength)
		
		
		
		

