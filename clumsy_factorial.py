n=int(input())
f=list(range(n,0,-1))
ans=""
mul=0
div=1
plus=2
sub=3

for i in range(len(f)-1):
	if i==mul:
		ans+=(str(f[i])+'*')
		mul+=4
	
	if i==div:
		ans+=(str(f[i])+'//')
		div+=4
	
	if i==plus:
		ans+=(str(f[i])+'+')
		plus+=4
	
	if i==sub:
		ans+=(str(f[i])+'-')
		sub+=4
	
ans+='1'
print(eval(ans))