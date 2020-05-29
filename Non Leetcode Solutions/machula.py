t=int(input())
for i in range(t):
    l=input()
    s=input()
    x=s.split('+')
    a=x[0]
    b,c=x[1].split('=')
    if 'machula' in c:
        print(a,'+',b,'= ',str(int(a)+int(b)),sep="")
    elif 'machula' in b:
        print(a,'+',' '+str(int(c)-int(a)),' =',c,sep="")
    elif 'machula' in a:
        print(str(int(c)-int(b)),' +',b,'=',c,sep="")
        
