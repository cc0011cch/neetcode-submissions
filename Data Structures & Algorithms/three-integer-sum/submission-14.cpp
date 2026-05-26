#include<ranges>
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        vector<vector<int>> rlt;
        for(auto&& [idx,num]: std::views::enumerate(nums)){
            if (num>0) break;
            if (idx>0 and num==nums[idx-1]) continue;
            auto l{idx+1};
            auto r{nums.size()-1};
            while (l<r){
                int target = num + nums[l] + nums[r];
                if (target >0) r--;
                else if (target < 0) l++;
                else {
                    rlt.emplace_back(vector<int>({num, nums[l], nums[r]}));
                    l++,r--;
                    while (l<r and nums[l]==nums[l-1]) l++;
                }
            }
        }
        return rlt;
    }
};
