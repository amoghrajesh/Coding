l=list(map(int,input().split()))
zero=0
one=0
two=0
for i in l:
    if i==0:
        zero+=1
    elif i==1:
        one+=1
    else:
        two+=1
j=0
while zero:
    l[j]=0
    zero-=1
    j+=1
while one:
    l[j]=1
    one-=1
    j+=1
while two:
    l[j]=2
    two-=1
    j+=1
print(l)
