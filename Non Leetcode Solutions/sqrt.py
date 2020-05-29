import math
a=int(input())
b=int(input())
c=int(input())
D=((b*b)-(4*a*c))
x1=(-b+math.sqrt(D))/(2*a)
x2=(-b-math.sqrt(D))/(2*a)
print(round(x1))
print(round(x2))
