class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> rlt(nums.size(),1);
        for (int i=0; i!=nums.size()-1; i++) rlt[i+1]=rlt[i]*nums[i];
        unsigned int tmp{1};
        for (int i=nums.size()-1; i>=0 ;i--){
            rlt[i]*=tmp;
            tmp*=nums[i];
        }
        return rlt;
    }
};
