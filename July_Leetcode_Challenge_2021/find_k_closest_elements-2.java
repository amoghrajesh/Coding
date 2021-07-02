class Solution {
    public int binarySearch(int[] arr, int n, int x){
        int l = 0;
        int r = n - 1;
        int mid = 0;
        
        while(l <= r){
            mid = l + (r - l)/2;
            if(arr[mid] == x){
                return mid;
            }
            else if(arr[mid] > x){
                r = mid - 1;
            }
            else{
                l = mid + 1;
            }
        }
        return mid;
    }
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> ans = new ArrayList<>();
        int n = arr.length;
        if(n == 0){
            return ans;
        }
        if (n == k) {
            for (int i = 0; i < k; i++) {
            ans.add(arr[i]);
            }
            return ans;
        }
         
        int index = binarySearch(arr, n, x);
        
        int l = Math.max(0, index - 1);
        int r = l + 1;
        
        while(r - l - 1 < k){
            if(l == -1){
                r++;
                continue;
            }
            if(r == n || (Math.abs(arr[l] - x) <= Math.abs(arr[r] - x))){
                l--;
            }
            else{
                r++;
            }
        }
        
        for(int i = l + 1; i < r; i++){
            ans.add(arr[i]);
        }
        
        return ans;
        
    }
}
