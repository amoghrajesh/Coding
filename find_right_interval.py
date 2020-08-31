class Solution(object):
    def bs(self, key, a, l, r):
        while l < r:
            m = l + (r - l)//2
            if a[m][0] == key:
                return m
            elif a[m][0] < key:
                l = m + 1
            else:
                r = m
        return l
        
        
        
    def findRightInterval(self, a):
        n = len(a)
        if not a:
            return []
        hashmap = dict()
        for i in range(n):
            hashmap[tuple(a[i])] = i
        
        a.sort(hashmap.keys()[0], key = lambda x: (x[0], x[1]))
        ans = [-1] * n
        for i in range(n - 1):
            x = self.bs(a[i][1], a, i + 1, n)
            if x < n:
                ans[hashmap[a[x]]] = hashmap[a[x]]
        ans[a[-1][1]] = -1
        return ans
                
                
            
                
        