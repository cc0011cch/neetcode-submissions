class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mprofit= 0
        bestBuy=prices[0]
        for cur in prices:
            mprofit = max(cur-bestBuy, mprofit)
            if bestBuy> cur: bestBuy= cur
        return mprofit
        