#include<stack>
class Solution {
public:
    bool same_sign(int a, int b){
        return (a < 0 && b < 0) || (a > 0 && b > 0);
    }
    
    vector<int> asteroidCollision(vector<int>& asteroids) {
        int n = asteroids.size();
        if(!n){
            return asteroids;
        }
        stack<int> st;
        for(int i = 0; i < n; i++){
            int f = 0;
            if(i == 0 && st.empty()){
                st.push(asteroids[i]);
            }
            
            else{
                if(same_sign(asteroids[i], st.top())){
                    st.push(asteroids[i]);
                }
                else{
                    if(st.top() < 0){
                        st.push(asteroids[i]);
                    }
                    
                    else if(st.top() > 0 && asteroids[i] < 0){
                        if(st.top() == -asteroids[i]){
                            st.pop();
                        }
                        else if(st.top() < -asteroids[i]){
                            while(!st.empty() && asteroids[i] != st.top() && st.top() >0 && st.top() <= -asteroids[i]){
                                cout << "popping: " << st.top() << "\n"; 
                                if(st.top() == asteroids[i]){
                                    f = 1;
                                }
                                st.pop();
                            }
                                                 
                            if(!f && !(st.top() > -asteroids[i])){
                                st.push(asteroids[i]);
                            }
                            
                        }
                    }
                    else{
                        st.push(asteroids[i]);
                    }
                }
            }
            
        }
        
        
        
        vector<int> ans;
        while(!st.empty()){
            int x = st.top();
            st.pop();
            ans.push_back(x);
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};