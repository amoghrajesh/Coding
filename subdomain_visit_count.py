dom = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
hashmap = dict()
for i in dom:
    count, domain = i.split()
    domain = domain.split('.')
    for j in range(len(domain)):
        key = '.'.join(domain[j:])
        if key not in hashmap:
            hashmap[key] = int(count)
        else:
            hashmap[key] += int(count)
ans = []
for i in hashmap:
    ans.append(str(hashmap[i]) + " " + i)
print(ans)


