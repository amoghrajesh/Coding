#Recaman sequence
'''
    a(n)=a(n-1)-n
    if this is less than 0 or if this value has already appeared previously in the sequnece, a(n)=a(n-1)+n

'''
def recaman(n):
    l=[]
    l.append(0)
    for i in range(1,n+1):
        #print(l)
        a=l[i-1]-i
        #print(a)
        if a<=0 or a in l:
            a+=(2*i)
        l.append(a)
    return l

print("Recaman Seq:",recaman(20))

            
    
    
