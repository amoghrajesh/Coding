class Solution {
public:
    bool isRobotBounded(string instructions) {
        int x = 0;
        int y = 0;
        char direction = 'N';
        
        for(char c: instructions){
            if(c == 'L'){
                switch(direction){
                    case 'N': direction = 'W';
                            break;
                    case 'E': direction = 'N';
                            break;
                    case 'S': direction = 'E';
                            break;
                    case 'W': direction = 'S';
                            break;
                }
            }
            else if(c == 'R'){
                switch(direction){
                    case 'N': direction = 'E';
                            break;
                    case 'E': direction = 'S';
                            break;
                    case 'S': direction = 'W';
                            break;
                    case 'W': direction = 'N';
                            break;
                }
            }
            else if(c == 'G'){
                switch(direction){
                    case 'N': y++;
                            break;
                    case 'E': x++;
                            break;
                    case 'S': y--;
                            break;
                    case 'W': x--;
                            break;
                }
            }
        }
        
        return (x == 0 && y == 0) || (direction != 'N');
        
        
    }
};