#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> s;
        for(auto iter=nums.begin(); iter!=nums.end(); iter++){
            if (s.count(*iter)) return true;
            else s.emplace(*iter);
        }
        return false;
    }
};