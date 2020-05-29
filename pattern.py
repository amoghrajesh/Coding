def foo(word,pattern):
	capw=[]
	capp=[]
	w=word
	p=pattern
	for i in word:
		if i.isupper():
			capw.append(i)
		else:
			w+=i

	for i in pattern:
		if i.isupper():
			capp.append(i)
		else:
			p+=i

	i=0 
	j=0
	m=len(p)
	n=len(w)

	while j<m and i<n:
		if w[i]==p[j]:
			j+=1
		i+=1
	return j==m and capp==capw

n=int(input())
words=[]
for i in range(n):
	s=input()
	words.append(s)

pattern=input()
for word in words:
	ans=foo(word,pattern)
	if ans:
		print("true")
	else:
		print("false")
