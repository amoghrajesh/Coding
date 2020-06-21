logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
alog = []
nlog = []

for i in logs:
    j = i.split(' ')[1]
    if j.isnumeric():
        nlog.append(i)
    else:
        alog.append(i)

alog.sort(key = lambda x: (x.split()[1:],x.split()[0]))
print(alog  + nlog)
