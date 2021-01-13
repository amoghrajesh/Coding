class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int l = 0;
        int r = people.length - 1;
        int ans = 0;
        
        while(l <= r){
            if(people[l] + people[r] <= limit){
                ans++;
                l++;
                r--;
            }
            else if(people[r] <= limit){
                ans++;
                r--;
            }
        }
        
        return ans;
    }
}