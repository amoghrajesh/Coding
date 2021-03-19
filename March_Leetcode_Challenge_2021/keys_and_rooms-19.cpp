class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        if(!n){
            return true;
        }
        
        queue<int> q;
        vector<bool> visited(n, false);
        q.push(0);
        visited[0] = true;
        int curRoom;
        
        while(!q.empty()){
            curRoom = q.front();
            q.pop();
            
            for(int i = 0; i < rooms[curRoom].size(); i++){
                if(!visited[rooms[curRoom][i]]){
                    q.push(rooms[curRoom][i]);
                    visited[rooms[curRoom][i]] = true;
                }
            }
        }
        
        for(bool b: visited){
            if(!b){
                return false;
            }
        }
        return true;
    }
};
