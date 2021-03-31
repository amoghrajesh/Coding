class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        res = []
        ls, lt = list(stamp), list(target)
        m, n = len(stamp), len(target)
        
        def _check(start_ind):
            was_move = True
            for i in range(m):
                if ls[i] != lt[start_ind + i] and lt[start_ind + i] != '?':
                    was_move = False
                    break
            if was_move:
                res.append(start_ind)
                for i in range(m):
                    lt[start_ind + i] = '?'
                    
        
        for ind in range(n-m+1):
            _check(ind)
        for ind in range(n-m, -1, -1):
            _check(ind)
        
        
        return res[::-1] if "".join(lt) == '?' *n else []
