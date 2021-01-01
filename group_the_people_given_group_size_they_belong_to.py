class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap = dict()
        for i in range(len(groupSizes)):
            if groupSizes[i] != 1:
                if groupSizes[i] not in hashmap:
                    hashmap[groupSizes[i]] = [i]
                else:
                    hashmap[groupSizes[i]].append(i)
        
        ans = []
        for k in hashmap:
            v = hashmap[k]
            number_groups = len(v) // k
            start = 0
            for i in range(number_groups):
                ans.append(v[start: start + k])
                start = start + k
        
        for i in range(len(groupSizes)):
            if groupSizes[i] == 1:
                ans.append([i])
        return ans