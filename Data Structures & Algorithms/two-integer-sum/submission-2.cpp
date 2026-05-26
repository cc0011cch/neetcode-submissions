#include <algorithm>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i{0};
        for(auto iter{nums.begin()}; iter!=nums.end(); i++,iter++){
            int j{i+1};
            auto iter1 = iter + 1;
            
            for(; iter1!=nums.end(); j++, iter1++)
                if (target-*iter== *iter1)
                return vector<int>{i, j};
        }
    }
};
