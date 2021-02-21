class Solution {
    public int brokenCalc(int X, int Y) {
        int level = 0;
        while(X < Y){
            if(Y % 2 == 0){
                Y = Y / 2;
            }
            else{
                Y++;
            }
            level = level + 1;
        }
        return level + X - Y;
    }
}
