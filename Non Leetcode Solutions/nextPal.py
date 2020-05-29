# your code goes here
def is_palindrome(n):
    if len(n) <= 1:
        return False
    else:
        m = len(n)//2
        for i in range(m):
            j = i + 1
            if n[i] != n[-j]:
                return False
        return True

def next_palindrome(n):
    if not n:
        return False
    else:
        if is_palindrome(n) is True:
            return n
        else:
           return next_palindrome(str(int(n)+1))

t=int(input())
for i in range(t):
    n=input()
    print(next_palindrome(n))
