from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adjacent = defaultdict(list)
        wordToIndex = dict()
        
        for i in range(len(wordList)):
            wordToIndex[wordList[i]] = i
        
        visited = [False] * len(wordList)
        
        temp = []
        for i in wordList:
            uncommon = 0
            for j in range(len(beginWord)):
                if beginWord[j] != i[j]:
                    uncommon += 1
            if uncommon == 1:
                temp.append(i)
        
        adjacent[beginWord] = temp
        
        for i in range(len(wordList)):
            u = wordList[i]
            for j in range(i + 1, len(wordList)):
                v = wordList[j]
                uncommon = 0
                
                for k in range(len(u)):
                    if u[k] != v[k]:
                        uncommon += 1
                if uncommon == 1:
                    adjacent[u].append(v)
                    adjacent[v].append(u)
                    
        print(adjacent)
        Q = list()
        Q.append(beginWord)
        if not adjacent[Q[0]]:
            return 0
        level = 1
        
        while Q:
            size = len(Q)
            while size:
                front = Q.pop(0)
                for adj in adjacent[front]:
                    if adj == endWord:
                        return level + 1
                    if not visited[wordToIndex[adj]]:
                        Q.append(adj)
                        visited[wordToIndex[adj]] = True
                size -= 1
            level += 1
        return 0