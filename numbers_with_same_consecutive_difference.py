class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return list(range(0, 10))
        q = list(range(1, 10))
        
        for level in range(N - 1):
            next_q = []
            for num in q:
                tail = num % 10
                next_dig = set([tail + K, tail - K])
                
                for d in next_dig:
                    if  0 <= d <= 9:
                        new = num * 10 + d
                        next_q.append(new)
            q = next_q
        return q