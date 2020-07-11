def closest_point():
m,n = list(map(int, input().split()))
k = int(input())
pts = xs = ys = []
for i in range(k):
    temp = list(map(int, input().split()))
    x,y = temp
    pts.append(temp)
    xs.append(x)
    ys.append(y)

xmax = max(xs)
ymax = max(ys)
perp = []
for p in pts:
    x,y = p
    top, left, right, bottom = m -y, x, n - x, y
    perp.append([top, left, right, bottom])
    closest_point()