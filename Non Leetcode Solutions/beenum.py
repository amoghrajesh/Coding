while True:
    f=0
    x=int(input())
    if x==-1:
        break
    if x==1:
        print('Y')
    else:
        x-=1
        i=1
        while x>0:
            x-=(6*i)
            i+=1
        if x==0:
            print('Y')
        else:
            print('N')
            
    
            
