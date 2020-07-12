class Solution:
    def reverseBits(self, n: int) -> int:
        stack = []
        while n:
            x = n % 2
            n//=2
            stack.append(str(x))
        stack = stack[::] + ['0'] * (32 - len(stack))
        b = ''.join(stack)
        return int(b, 2)