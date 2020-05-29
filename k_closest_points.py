l=[[3,3],[5,-1],[-2,4]]
k=2
temp=[]
for i in l:
	x=((i[0]**2+i[1]**2)**0.5,i)
	temp.append(x)

temp=sorted(temp,key=lambda x:x[0])
ans=temp[:k]
for i in range(len(ans)):
	ans[i]=ans[i][1]
return ans
