num=int(input())
ans=[0,1,1]
no_of_bits_for_i=2

for i in range(3,num+1):
	if i>=no_of_bits_for_i*2:
		c=no_of_bits_for_i*2
	ans.append(ans[i%no_of_bits_for_i]+1)
print(ans)
