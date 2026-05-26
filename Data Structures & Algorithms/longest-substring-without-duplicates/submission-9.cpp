class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string rs="";
        int  maxcount{0};
        for(auto c:s){
            size_t idx = rs.find(c);
            if (idx == std::string::npos) 
                rs=rs+c;
            else{
                rs=rs.substr(idx+1, s.size())+c;
            }
            maxcount=max(maxcount, static_cast<int>(rs.size()) );
        }
        return maxcount;
    }
};
