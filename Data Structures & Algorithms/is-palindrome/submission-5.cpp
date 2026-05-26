class Solution {
public:
    bool isPalindrome(string s) {
        string unique_s;
        for(auto c:s) 
            if (isalnum(c)) unique_s+=tolower(c);
        int first{0};
        int last{int(unique_s.size())-1};
        while (first <last){
            if (unique_s[first]==unique_s[last]){
                first++;
                last--;
            }
            else return false;
        }
        return true;
        
    }
};
