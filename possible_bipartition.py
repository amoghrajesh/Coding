N = 4
dislikes = [[1,2],[1,3],[2,4]]

red = [dislikes[0][0]]
blue = [dislikes[0][1]]

for i in range(1,len(dislikes)):
    v1, v2 = dislikes[i]
    if v1 in red:
        blue.append(v2)
    elif v1 in blue:
        red.append(v2)
    elif v2 in red:
        blue.append(v1)
    elif v2 in blue:
        red.append(v1)
    else:
        red.append(v1)
        blue.append(v2)

s1 = set(red)
s2 = set(blue)
s3 = len(s1.intersection(s2))
if s3 ==0:
    print(True)
else:
    print(False)
