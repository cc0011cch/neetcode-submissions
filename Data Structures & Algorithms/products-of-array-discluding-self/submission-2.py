class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]
        for num in nums[:-1]:
            ans.append(ans[-1]*num)
        tmp=1
        for idx,rnum in enumerate(nums[::-1]):
            ans[len(ans)-idx-1]*=tmp
            tmp*=rnum

        return ans