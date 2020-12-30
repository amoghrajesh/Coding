class Solution {
public:
    int processDeadCell(vector<vector<int>> &board, int i, int j){
        int liveCells = 0;
            
        
         for(int ind = 0; ind < 8; ++ind){
            if((i+xcoord[ind] < 0) || (i+xcoord[ind] >= board.size()))
                continue;
            
            if((j+ycoord[ind] <0) || (j+ycoord[ind] >= board[0].size()))
                continue;  
             
             
            if(board[i+xcoord[ind]][j+ycoord[ind]] == 1 || 
                board[i+xcoord[ind]][j+ycoord[ind]] == -1)
                liveCells++;
        }
        return liveCells == 3 ? -2 : 0;        
    }
    
    int processLiveCell(vector<vector<int>> &board, int i, int j){
        int liveCells = 0;
        for(int ind = 0; ind < 8; ++ind){
            if((i+xcoord[ind] < 0) || (i+xcoord[ind] >= board.size()))
                continue;
            
            if((j+ycoord[ind] <0) || (j+ycoord[ind] >= board[0].size()))
                continue;
            
            if(board[i+xcoord[ind]][j+ycoord[ind]] == 1 || 
                board[i+xcoord[ind]][j+ycoord[ind]] == -1)
                liveCells++;
        }
        
        if(liveCells < 2)
            return -1;
        else if(liveCells == 2 || liveCells == 3)
            return 1;
        else if(liveCells > 3)
            return -1;
        else
            return 1;       
        
    }
    int findVal(vector<vector<int>> &board, int i, int j){
        if(board[i][j] == 0)
            return processDeadCell(board, i, j);
        else
            return processLiveCell(board, i, j);
    }
    void gameOfLife(vector<vector<int>>& board) {
        for(int i=0; i<board.size(); ++i){
            for(int j=0; j<board[0].size(); ++j){
                board[i][j] = findVal(board, i, j);            
            }
        }
        
        for(int i=0; i<board.size(); ++i){
            for(int j=0; j<board[0].size(); ++j){
                if(board[i][j] == -1)
                    board[i][j] = 0;
                else if(board[i][j] == -2)
                    board[i][j] = 1;
            }
        }        
        
    }
    private:
    vector<int> xcoord = {-1, -1, -1, 0, 1, 1, 1,  0};
    vector<int> ycoord = {-1, 0,   1, 1, 1, 0, -1, -1};
};