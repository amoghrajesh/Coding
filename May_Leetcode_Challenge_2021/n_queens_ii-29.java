class Solution {
    int ans;
    boolean[][] board;
    
    public int totalNQueens(int N) {
        ans = 0;
        board = new boolean[N][N];
        place(0,0,0,0);
        return ans;
    }
    
    private void place(int i, int vert, int ldiag, int rdiag) {
        int N = board.length;
        if (i == N) ans++;
        else for (int j = 0; j < N; j++) {
            int vmask = 1 << j, lmask = 1 << (i+j), rmask = 1 << (N-i-1+j);
            if ((vert & vmask) + (ldiag & lmask) + (rdiag & rmask) > 0) continue;
            board[i][j] = true;
            place(i+1, vert | vmask, ldiag | lmask, rdiag | rmask);
            board[i][j] = false;
        }
    }
}
