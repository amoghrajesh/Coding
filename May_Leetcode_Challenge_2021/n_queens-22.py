class Solution:
    def __init__(self, ans = None):
        self.ans = []
		
		
    def solveNQueens(self, n):
        arr = [['.' for i in range(n)] for i in range(n)]
        self.nQueen(arr,0,n)
        return self.ans
    
    def isSafe(self,arr,x,y,n):
        for row in range(x):
            if arr[row][y]=='Q':
                return False
        row = x
        col= y
        while row>=0 and col>=0:
            if arr[row][col]=='Q':
                return False
            row-=1
            col-=1
        row=x
        col=y
        while row>=0 and col<n:
            if arr[row][col]=='Q':
                return False
            row-=1
            col+=1
        return True
    
    def nQueen(self,arr,x,n):
        if x>=n:
            self.ans.append(["".join(arr[i]) for i in range(n)])
            return None
        for col in range(n):
            if self.isSafe(arr,x,col,n):
                arr[x][col]='Q'
                if self.nQueen(arr,x+1,n):
                    return True
                arr[x][col]='.'
        return False
