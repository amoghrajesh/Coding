#include <cstdlib>
#include <algorithm>
class Solution {
public:
    double angleClock(int hour, int minutes) {
        double angle_hour = (60 * hour + minutes)/2.0;
        double angle_minute = minutes * 6;
        
        double angle = abs(angle_hour - angle_minute);
        return min(angle, 360 - angle);
        
    }
};