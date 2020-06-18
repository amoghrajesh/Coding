def validIPAddress(s):
    nums = '0123456789'
    small = 'abcdef'
    if '.' in s:
        parts = s.split('.')
        if len(parts)!=4:
            return "Neither"
        for i in parts:
            if len(i)==0:
                return "Neither"
            else:
                if i[0] == '0':
                    return "Neither"
                else:
                    for j in i:
                        if j.isalpha():
                            return "Neither"
                    if not 0<=int(i)<=255:
                        return "Neither"
        return "IPv4"
    else:
        parts = s.split(':')
        print(parts)
        if len(parts)!=8:
            return "Neither"
        
        for i in parts:
            n = len(i)
            print(i, n)
            if n==0:
                return "Neither"
            elif n>4:
                return "Neither"
            else:
                for j in i:
                    if j.isalpha():
                        if j.lower() not in small:
                            return "Neither"
        return "IPv6"

print(validIPAddress(input()))