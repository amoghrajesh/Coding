emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
ans = []
for email in emails:
    data = email.split('@')[0]
    url = email.split('@')[1]
    n = len(data)
    i = 0
    s = ''
    while i<n and data[i]!='+':
        if data[i]!='.':
            s+=data[i]
        i+=1
    ans.append(s+url)
print(ans)
print(len(set(ans)))