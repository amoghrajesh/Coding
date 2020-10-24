class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int P) {
        int score = 0;
        int l = 0;
        int r = tokens.size() - 1;
        sort(tokens.begin(), tokens.end());
        
        if(r == -1 || P < tokens[0]){
            return score;
        }
        
        
        
        while(l <= r){
            while(l <= r && tokens[l] <= P){
                score++;
                P -= tokens[l];
                l++;
            }
            
            if(r > l){
                P += tokens[r];
                r--;
                score--;
            }
            else{
                break;
            }
        }
        return score;
    }
};