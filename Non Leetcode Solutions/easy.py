a,b=input().split()
a,b=int(a),int(b)
x=a-b
l=list(str(x))
l[-1]=str(int(l[-1])^2)
print(int("".join(l)))
