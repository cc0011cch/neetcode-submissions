#include <ranges>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int,int>counts;
        for(const auto n:nums){
            counts[n]++;
        }
        
        std::vector<std::vector<int>> freq(nums.size()+1);
        for(const auto&[n, c]: counts){
            freq[c].push_back(n);
        }
        std::vector<int>output;
        for(const auto& v: std::views::reverse(freq)){
            for(const auto c: v){
               output.push_back(c);
                if (output.size()==k) return output;
            }
        }
        return output;
    }
};
