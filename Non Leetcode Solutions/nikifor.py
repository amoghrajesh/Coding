n=input()
if '0' in n:
    print(2)
else:
    print(1)
    x=range(1,10)
    for i in x:
        if '0' in str(abs(int(n)-i)):
            print(i)
            break
    
    
