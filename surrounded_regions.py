def dfs(board, i, j):
    if i<0 or i>=len(board) or j < 0 or j>=len(board[i]) or board[i][j] == 'X':
        return
    
    board[i][j] = '$'
    print("done")
    dfs(board, i, j-1)
    dfs(board, i-1, j)
    dfs(board, i, j+1)
    dfs(board, i+1, j)
    return board

def solve(board):
    if not board:
        return None
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i==0 or i==(len(board)-1) or j==0 or j == (len(board[i]) - 1):
                if board[i][j] == '0':
                    dfs(board, i, j)
    print(board)


board = [['X','X', 'X', 'X'],
['X', 'O', 'O', 'X'],
['X', 'X', 'O', 'X'],
['X','O', 'X', 'X']]

print(solve(board))