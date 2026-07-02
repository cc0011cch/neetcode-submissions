class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mprofit= 0
        l,r = 0,1
        while r < len(prices):
            if prices[l]<prices[r]:
                mprofit = max(prices[r]-prices[l], mprofit)
            else:
                l=r
            r+=1
        return mprofit
#        bestBuy=prices[0]
#        for cur in prices:
#            mprofit = max(cur-bestBuy, mprofit)
#            if bestBuy> cur: bestBuy= cur
#        return mprofit
#Input: prices = [10,1,5,6,7,1]

#Output: 6        
        