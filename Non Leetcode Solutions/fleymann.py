while True:
    x=int(input())
    if x==0:
        break
    y=x*(x+1)*(2*x+1)
    y=y//6
    print(y)
