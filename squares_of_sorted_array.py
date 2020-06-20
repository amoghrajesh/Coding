l = [-4,-1,0,3,10]
n = len(l)
beg = 0
end = n-1

ans = []
while beg<=end:
    b = l[beg]**2
    e = l[end]**2

    if b < e:
        print("in")
        ans.append(e)
        end-=1
    else:
        ans.append(b)
        beg+=1

print(ans[::-1])