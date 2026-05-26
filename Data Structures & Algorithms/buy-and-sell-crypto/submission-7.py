class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mprofit= 0
        l =0
        for r in range(1, len(prices)):
            mprofit = max(prices[r]- prices[l],mprofit)
            if prices[l]> prices[r]: l=r
        return mprofit
        