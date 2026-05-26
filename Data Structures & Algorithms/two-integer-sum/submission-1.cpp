#include <algorithm>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i{0};
        for(auto iter{nums.begin()}; iter!=nums.end(); i++,iter++){
            int reminder= target - *iter;
            auto itf=std::find(iter+1, nums.end(),reminder);
            if (itf!=nums.end())
                return vector<int>{i, i+int(distance(iter+1, itf))+1};
        }
    }
};
