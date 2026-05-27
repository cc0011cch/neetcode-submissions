class Solution {
public:
    bool isValid(string s) {
        unordered_map<char,char> open2close={
            {'(',')'},
            {'[',']'},
            {'{','}'},                        
        };
        stack<char> stacks;
        for(auto c : s){
            if (open2close.contains(c))
                stacks.push(open2close[c]);
            else{
                if (stacks.empty()) return false;
                if (c == stacks.top()) {
                    stacks.pop();
                }else return false;
            }
        }
        if (!stacks.empty()) return false;
        return true;
    }
};
