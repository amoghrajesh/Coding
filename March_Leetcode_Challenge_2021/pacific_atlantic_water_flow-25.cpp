class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
      if (matrix.empty()) return {};
    const int n = matrix.size();
    const int m = matrix[0].size();
    
    const vector<int> dirs{0, 1, 0, -1, 0};
        
    auto bfs = [&](queue<pair<int, int>>& q, vector<vector<int>>& v) {
      while (!q.empty()) {
        const int y = q.front().first;
        const int x = q.front().second;        
        q.pop();
        const int h = matrix[y][x];
        v[y][x] = true;
        for (int i = 0; i < 4; ++i) {
          int tx = x + dirs[i];
          int ty = y + dirs[i + 1];
          if (tx < 0 || ty < 0 || tx == m || ty == n || matrix[ty][tx] < h) continue;
          if (v[ty][tx]) continue;
          q.push({ty, tx});
        }
      }
    };
    
    queue<pair<int, int>> qp;
    queue<pair<int, int>> qa;
    vector<vector<int>> vp(n, vector<int>(m));
    vector<vector<int>> va(n, vector<int>(m));    
    
    for (int x = 0; x < m; ++x) {
      qp.push({0, x}); // top
      qa.push({n - 1, x}); // bottom   
    }
    
    for (int y = 0; y < n; ++y) {
      qp.push({y, 0}); // left
      qa.push({y, m - 1}); // right      
    }
    
    bfs(qp, vp);
    bfs(qa, va);    
    
    //vector<pair<int, int>> ans;
    vector<vector<int>> ans;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j)
        if (vp[i][j] && va[i][j]) //ans.emplace_back(i, j);
                  ans.push_back({i,j});
    return ans;
    }
};
