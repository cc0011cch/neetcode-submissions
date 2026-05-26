#include<ranges>
class Solution {
public:
    int characterReplacement(string s, int k) {
           unordered_map<char, int> count;
           int longest{0}, l{0}, maxfqt{0};
           for(auto&& [r, c]: std::views::enumerate(s)){
                count[c]++;
                maxfqt= max(maxfqt, count[c]);
                while (static_cast<int>(r)-l+1-maxfqt>k){
                    count[s[l]]--;
                    l++;
                }

                longest=max(static_cast<int>(r)-l+1, longest);
           }
           
            return longest;
    }
};
