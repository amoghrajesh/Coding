import re
s = """123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] \"GET /pics/wpaper.gif HTTP/1.0\" 200 6248 \"http:// www.jafsoft.com/asctortf/\" \"Mozilla/4.05 (Macintosh; I; PPC)"""
for i in s.split():
    print(i)

print(re.findall('([0-9]+ [0-9]+)', s))