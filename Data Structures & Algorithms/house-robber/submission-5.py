class Solution:
    def rob(self, nums: List[int]) -> int:

        a, b =0,0 
        for i in nums:
            temp=b
            b=max(b,a+i)
            a=temp

        return b