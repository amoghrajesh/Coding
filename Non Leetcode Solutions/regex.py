import re
s="412345"
match=re.search(r'[789]\d+',s)
if match:
    print('found')
    print(match.group())
else:
    print("not found")
