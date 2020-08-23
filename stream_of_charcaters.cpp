typedef struct TrieNode{
    bool end;
    TrieNode* next[26];
    TrieNode(){
        end = false;
        for(int i  = 0; i < 26; i++){
            next[i] = NULL;
        }
    }
}TrieNode;


class StreamChecker {
public:
    TrieNode* root = new TrieNode();
    string s = "";
    StreamChecker(vector<string>& words) {
        for(string w: words){
            reverse(w.begin(), w.end());
            TrieNode* temp = root;
            for(int i = 0; i < w.size(); i++){
                if(temp->next[w[i] - 'a'] == NULL){
                    temp->next[w[i] - 'a'] = new TrieNode();
                }
                temp = temp->next[w[i] - 'a'];
            }
            temp->end = true;
        }
    }
    
    bool isfound(TrieNode* p, string t){        
        for(int i = t.size() - 1; i > -1; i--){
            if(!p->next[t[i] - 'a']){
                return false;
            }
            else{
                p = p->next[t[i] - 'a'];
                if(p->end){
                    return true;
                }
            }
        }
        return p->end;
        
        
    }
    
    bool query(char letter) {
        
        s += letter;
        return isfound(root, s);
        
        
    }
};
