from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        maxB = Counter()
        for b in B:
            temp = Counter(b)
            for key in temp:
                maxB[key] = max(maxB.get(key, 0), temp[key])
        
        ans = []
        for a in A:
            # is maxB subset of me?
            temp = Counter(a)
            subset = True
            for key in maxB:
                if key not in temp or (key in temp and temp[key] < maxB[key]):
                    subset = False
            if subset:
                ans.append(a)
        return ans   
