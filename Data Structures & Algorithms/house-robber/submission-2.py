class Solution:
    def rob(self, nums: List[int]) -> int:

        len_lst=len(nums)
        if len(nums)%2: len_lst-=1
        a, b =0,0 
        for i in nums:
            a,b=b, max(b,a+i)

        print(a, b)
        return b