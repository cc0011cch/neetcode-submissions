#include <ranges>
class Solution {
public:
    string minWindow(string s, string t) {
        int l{0};
        int formed{0};
        vector<int> ans={INT_MAX, -1, -1};
        
        unordered_map<char, int>tmap, smap;
        for (auto c:t) tmap[c]++; 
        int required=tmap.size();

        for (auto&& [r,c]: std::views::enumerate(s)){
            if (tmap.contains(c)) smap[c]++;
            if (tmap.contains(c) and smap[c]==tmap[c]) formed ++;
            while (l<= static_cast<int>(r) and required==formed){
                if (r-l+1 <ans[0]) {
                    ans[0]=r-l+1;
                    ans[1]=l;
                    ans[2]=r;
                }
                if (tmap.contains(s[l]))
                    smap[s[l]]--;
                if (tmap.contains(s[l]) and smap[s[l]]< tmap[s[l]]) formed--;

                l++;
            }
        }
        return (ans[0]==INT_MAX)? "": s.substr(ans[1],ans[0]);
    }
};
