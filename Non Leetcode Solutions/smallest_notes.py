t=int(input())
for i in range(t):
    n=int(input())
    n1=n//100
    r1=n%100
    n2=r1//50
    r2=r1%50
    n3=r2//10
    r3=r2%10
    n4=r3//5
    r4=r3%5
    n5=r4//2
    r5=r4%2
    n6=r5//1
    r6=r5%1
    print(n1+n2+n3+n4+n5)
    
