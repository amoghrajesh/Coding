l=[1,2,3,4,5,6,7,8,9]
n=len(l)
#if n<2:
#	return n
diff=[]
for i in range(1,n):
	d=l[i]-l[i-1]
	if d==0:
		diff.append(0)
	elif d>0:
		diff.append(1)
	else:
		diff.append(-1)

stack=[]
p=0
while p<n-1:
	if diff[p]!=stack[-1]:
		stack.append(diff[p])
	p+=1

ans=0
for i in stack:
	if i!=0:
		ans+=1
print(ans+1)
#return ans+1