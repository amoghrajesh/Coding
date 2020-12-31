#include<stack>
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> s;
        int i = 0;
        int n = heights.size();
        
        if(!n){
            return 0;
        }
        if(n == 1){
            return heights[0];
        }
        
        int maxarea = 0;
        int area;
        int width;
        
        
        while(i < n){
            if(s.empty() || heights[s.top()] <= heights[i]){
                s.push(i);
                i++;
            }
            else{
                int top = s.top();
                s.pop();
                
                if(s.empty()){
                    width = i;
                }
                else{
                    width = i - s.top() - 1;
                }
                
                area = heights[top] * width;
                maxarea = max(maxarea, area);
                
            }
        }
        
        while(!s.empty()){
                int top = s.top();
                s.pop();
                
                if(s.empty()){
                    width = i;
                }
                else{
                    width = i - s.top() - 1;
                }
                
                area = heights[top] * width;
                maxarea = max(maxarea, area);
        }
        
        return maxarea;
    }
};