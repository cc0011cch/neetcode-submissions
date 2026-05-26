class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size()==0) return 0;
        int longest{1}, length{1};
        std::set<int> unique_nums(nums.begin(),nums.end());
        std::vector<int> sort_nums(unique_nums.begin(),unique_nums.end());
        for(int i=1; i!=sort_nums.size();i++){
            if(sort_nums[i]-sort_nums[i-1]==1)
                length++;
            else length=1;
            if (longest<length) longest=length;
        }
        return longest;

    }
};
