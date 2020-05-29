key={'c','h','e','f'}
t=int(input())
for i in range(t):
    s=input()
    c=0
    l=[]
    for j in range(len(s)-3):
        l=[]
        l.append(s[j])
        l.append(s[j+1])
        l.append(s[j+2])
        l.append(s[j+3])
        x=set(l)
        print(x)
        if(x==key):
            c+=1
    if(c==0):
        print("normal")
    else:
        print("lovely",c)
        

        
        
