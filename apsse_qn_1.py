n=int(input())
l=[0,0,0,1,3]
for i in range(5,n+1):
	t=2*l[i-1]+2**(i-4)-l[i-4]
	l.append(t)
print(l)

#1144313558794471391
#2,147,483,647
#9223372036854775807


#Expected--> 1144313558794471391
#102686354170415071
