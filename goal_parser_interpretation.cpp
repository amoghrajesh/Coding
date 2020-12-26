class Solution {
public:
    string interpret(string command) {
        string ans = "";
        int i = 0;
        int n = command.size();
        
        while(i < n){
            if(command[i] == 'G'){
                ans += "G";
                i++;
            }
            else if(command[i] == '('){
                if(i + 1 < n && command[i + 1] == ')'){
                    ans += "o";
                    i = i + 2;
                }
                else if(i + 3 < n && command[i + 3] == ')'){
                    ans += "al";
                    i = i + 4;
                }
            }
        }
        return ans;
    }
};