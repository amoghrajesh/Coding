class RecentCounter {
public:
    queue<int> q;
    RecentCounter() {
        q = {};   
    }
    
    int ping(int t) {
        q.push(t);
        while(!q.empty()){
            // if out of range then pop off
            int f = q.front();
            if(f < (t - 3000) or f > t){
                q.pop();
            }
            else{
                break;
            }
        }
        return q.size();
    }
};