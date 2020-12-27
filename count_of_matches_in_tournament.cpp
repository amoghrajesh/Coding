class Solution {
public:
    int numberOfMatches(int n) {
        int teams, matches;
        teams = n;
        matches = 0;
        
        while(teams != 1){
            // cout << teams << " " << matches << "\n";
            if(teams % 2 == 0){
                matches += teams / 2;
                teams = teams / 2;
            }
            else{
                matches += (teams - 1) / 2;
                teams = (teams - 1)/2 + 1;
            }
        }
        return matches;
    }
};