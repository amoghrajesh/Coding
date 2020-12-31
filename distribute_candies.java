class Solution {
    public int distributeCandies(int[] candyType) {
        Set<Integer> s = new HashSet<Integer>();
        int n = candyType.length;
        for(int c: candyType){
            s.add(c);
        }
        
        return Math.min(s.size(), n / 2);
    }
}