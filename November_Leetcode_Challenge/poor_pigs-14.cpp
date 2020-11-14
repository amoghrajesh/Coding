#include<cmath>
class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int x = 0;
        int periods = minutesToTest / minutesToDie;
        
        while((int)pow(periods + 1, x) < buckets){
            x++;
        }
        return x;
    }
};