class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int drank = numBottles;
        int full = 0;
        
        while(numBottles >= numExchange){
            full = numBottles / numExchange;
            drank += full;
            numBottles = full + (numBottles % numExchange);
        }
        return drank;
    }
}