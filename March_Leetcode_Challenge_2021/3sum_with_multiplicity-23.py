from collections import Counter 
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        f = Counter(arr)
        keys = sorted(list(f.keys()))
        
        n = len(keys)
        ans = 0
        
        for i in range(n - 1):
            a = keys[i]
            bplusc = target - a
            j = i
            k = n - 1
            
            while j <= k:
                b = keys[j]
                c = keys[k]
                
                if b + c < bplusc:
                    j += 1
                elif b + c > bplusc:
                    k -= 1
                elif b + c == bplusc:
                    if i < j < k:
                        ans += (f[a] * f[b] * f[c])
                    elif i == j < k:
                        ans += (f[a] * (f[a] - 1)) // 2 * f[c]
                    elif i < j == k:
                        ans += f[a] * (f[b] * (f[b] - 1)) // 2
                    elif i == j == k:
                        ans += (f[a] * (f[a] - 1) * (f[a] - 2)) // 6
                    j += 1
                    k -= 1
            return ans % (10 ** 9 + 7)
                    
        
