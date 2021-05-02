class Solution {
    public int scheduleCourse(int[][] courses) {
        int n = courses.length;
        int ans = 0;
        int t = 0;
        Arrays.sort(courses, (i, j) -> i[1] - j[1]);

        for(int i = 0; i < n; i++){
            if((t + courses[i][0]) <= courses[i][1]){
                t += courses[i][0];
                ans++;
            }
            else{
                int m = i;
                for(int j = 0; j < i; j++){
                    if(courses[j][0] > courses[m][0]){
                        m = j;
                    }
                }
                if(courses[i][0] < courses[m][0]){
                    t += courses[i][0] - courses[m][0];
                }
                
                courses[m][0] = -1;
                
            }
        }
        return ans;
    }
}
