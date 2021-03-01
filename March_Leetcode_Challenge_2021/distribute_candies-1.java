class Solution {
    public int distributeCandies(int[] candyType) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int keys = 0;
        for(int x: candyType){
            if(map.containsKey(x)){
                map.put(x, map.get(x) + 1);
            }
            else{
                map.put(x, 1);
                keys++;
            }
        }
        
        return Math.min(candyType.length / 2, keys);
    }
}
