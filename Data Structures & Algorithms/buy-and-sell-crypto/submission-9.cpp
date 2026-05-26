class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mprofit{0};
        int l{0};
        for (int r{1}; r<prices.size(); r++){

            mprofit= max(mprofit, prices[r]-prices[l]);
            if (prices[l]> prices[r]) l=r;
        }
        return mprofit;
    }
};
