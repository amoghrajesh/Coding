n=1000
t=[]
f=[]
both=[]
for i in range(1,n):
    if i%3==0 or i%5==0:
        both.append(i)

print(sum(both))

        
    
