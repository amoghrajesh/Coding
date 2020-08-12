u = [ "geek", "geek0", "geek1", "geek", "geek"]
hashmap = dict()
lastindex = 0
for i in u:
    if i not in hashmap:
        print(i)
        if i[-1].isdigit():
            hashmap[i] = i[-1]
            lastindex = int(i[-1]) + 1
        else:
            hashmap[i] = lastindex
    else:
        


