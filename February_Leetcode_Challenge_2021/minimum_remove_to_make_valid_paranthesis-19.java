class Solution {
    public boolean isParanthesis(char x){
        return x == '(' || x == ')';
    }
    
    public boolean isValidString(String s){
        int p = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '('){
                p++;
            }
            if(s.charAt(i) == ')'){
                p--;
            }
            if(p < 0){
                return false;
            }
        }
        return p == 0;
    }
    
    public String minRemoveToMakeValid(String s) {
        if(s.length() == 0){
            return s;
        }
        HashSet<String> visited = new HashSet<>();
        String temp; 
        Queue<String> q = new LinkedList<>();

        q.add(s); 
        visited.add(s); 
        while(!q.isEmpty()) 
        {
            s = q.peek(); 
            q.remove(); 
            if(isValidString(s)) 
            { 
                return s;
            } 
            for(int i = 0; i < s.length(); i++) 
            { 
                if((s.charAt(i) == '(' || s.charAt(i) == ')') == false) 
                    continue; 

                temp = s.substring(0, i) + s.substring(i + 1); 
                if(visited.contains(temp) == false) 
                { 
                    q.add(temp); 
                    visited.add(temp); 
                } 
            } 
        } 
        return "";
    }
}
