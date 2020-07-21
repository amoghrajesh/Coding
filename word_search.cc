class Solution {
public:
     bool dfs(int i,int j,int count,string& word,vector<vector<char>>& board){
         if(count==word.size())return true;
         if(i<0||i>=board.size()||j<0||j>=board[0].size()||board[i][j]!=word[count])return false;
         char temp=board[i][j];
         board[i][j]='#';
         bool answer=   dfs(i-1,j,count+1,word,board)||
                        dfs(i+1,j,count+1,word,board)||
                        dfs(i,j-1,count+1,word,board)||
                        dfs(i,j+1,count+1,word,board);
         board[i][j]=temp;
         return answer;
     }
    bool exist(vector<vector<char>>& board, string word) {
        for(int i=0;i<board.size();i++){
            for(int j=0;j<board[0].size();j++){
                if((board[i][j]==word[0])&&dfs(i,j,0,word,board))return true;
            }
        }
        return false;
    }
};