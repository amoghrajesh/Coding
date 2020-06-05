from random import random


class Solution:

    def __init__(self, l: List[int]):
        self.freq = [l[0]]
        for i in range(1, len(l)):
            self.freq.append(self.freq[-1] + l[i])
        self.last = self.freq[-1]

    def pickIndex(self) -> int:
        rand = random() * self.last
        l = 0
        r = len(self.freq)
        while l < r:
            m = l + (r - l) // 2
            if self.freq[m] > rand:
                r = m

            else:
                l = m + 1

        return l