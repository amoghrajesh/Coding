a=input()
b=input()
n=len(a)
temp=a
for i in range(n):
	temp=temp[1:]+temp[0]
	if temp==b:
		print("yes")
print("no")