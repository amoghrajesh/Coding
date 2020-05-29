ransomNote=input()
magazine=input()

ransom=dict()
mag=dict()

for i in ransomNote:
	if i not in ransom:
		ransom[i]=1
	else:
		ransom[i]+=1

for i in magazine:
	if i not in mag:
		mag[i]=1
	else:
		mag[i]+=1

#check now
for i in ransom:
	if i not in mag or ransom[i]>mag[i]:
		return False
return True

