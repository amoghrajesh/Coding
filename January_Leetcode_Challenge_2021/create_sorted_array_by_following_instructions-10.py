class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        limit=max(instructions)
        rangeQ=[0 for i in range(limit+1)]
        freq=collections.defaultdict(int)
        ans=0
        def update(val):
            while val<=limit:
                rangeQ[val]+=1
                val+=val & -val
        
        def Querry(val):
            res=0
            while val:
                res+=rangeQ[val]
                val-=val & -val
            return res
        for i,val in enumerate(instructions):
            update(val)
            freq[val]+=1
            lower=Querry(val-1)
            ans+=min(lower,i+1-lower-freq[val])
        return ans%(10**9+7)