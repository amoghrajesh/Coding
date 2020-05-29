t=int(input())
for i in range(t):
    n=int(input())
    fing=list(map(int,input().split()))
    glov=list(map(int,input().split()))
    f=0
    b=0
    if(fing[0]<=glov[0]):
              f=1
              for k in range(len(fing)):
                  if(fing[k]>glov[k]):
                      f=0
    if(fing[0]<=glov[n-1]):
              b=1
              for k in range(len(fing)):
                  if(fing[k]>glov[n-k-1]):
                      b=0
    if(f==0 and b==0):
              print("none")
    elif(f==0 and b==1):
              print("back")
    elif(f and b==0):
              print("front")
    elif(f==1 and b==1):
              print("both")
              
              
