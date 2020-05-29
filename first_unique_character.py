s=input()
hashmap=dict()
for i in s:
	if i not in hashmap:
		hashmap[i]=1
	else:
		hashmap[i]+=1
		
		
#find the unique element now
for i in range(len(s)):
	if hashmap[s[i]]==1:
		return i
return -1

