class Solution:
    def palind(self,i,j,string):
        return string[i:j] == string[i:j][::-1]
    
    def dfs(self,string,length,i,part):
        if i == length:
            self.result.append(part)
            
        for j in range(i+1,length+1):
            if self.palind(i,j,string):
                self.dfs(string,length,j,part + [string[i:j]])
                
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.dfs(s,len(s),0,[])
        return self.result