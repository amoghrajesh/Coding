class Solution {
    public boolean isValid(int x, int y, int n){
        return x > -1 && x < n && y > -1 && y < n;
    }
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if(grid[0][0] == 1){
            return -1;
        }
        boolean[][] visited = new boolean[n][n];
        
        int x = 0;
        int y = 0;
        int size;
        int[] temp;
        
        visited[x][y] = true;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        int level = 0;
        int nextX, nextY;
        
        while(q.isEmpty() == false){
            size = q.size();
            while(size-- != 0){
                temp = q.remove();
                if(temp[0] == n - 1 && temp[1] == n - 1){
                    return level + 1;
                }
                else{
                    for(int i = -1; i < 2; i++){
                        nextX = temp[0] + i;
                        for(int j = -1; j < 2; j++){
                            nextY = temp[1] + j;
                            if(isValid(nextX, nextY, n) && grid[nextX][nextY] == 0 && visited[nextX][nextY] == false){
                                q.add(new int[]{nextX, nextY});
                                visited[nextX][nextY] = true;
                            }
                        }
                    }
                }
            }
            level++;
        }
        return -1;
    }
}
