l=list(map(int,input().split()))
s=set(l)
expected_sum=3*(sum(list(s)))
curr_sum=sum(l)

return (expected_sum-curr_sum)//2

#hashmap=dict()
#for i in l:
#	if i in hashmap:
#		hashmap[i]+=1
#	else:
#		hashmap[i]=1
#
#for i in hashmap:
#	if hashmap[i]==1:
#		return i