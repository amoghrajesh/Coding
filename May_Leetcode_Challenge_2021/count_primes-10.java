class Solution {
    public int countPrimes(int n) {
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        
        for(int i = 2; i <= Math.ceil(Math.sqrt(n)); i++){
            if(isPrime[i]){
                int j = i * i;
                while(j <= n){
                    isPrime[j] = false;
                    j += i;
                }
            }
        }
        int ans = 0;
        
        for(int i = 2; i < n; i++){
            if(isPrime[i] == true){
                ans++;
            }
        }
        return ans;
    }
}
