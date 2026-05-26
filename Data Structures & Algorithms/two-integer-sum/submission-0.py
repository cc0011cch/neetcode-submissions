class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            for idx, n in enumerate(nums):
                reminder=target-n
                if reminder in nums[idx+1:]:
                    idx1=idx+1 + nums[idx+1:].index(reminder)
                    return [idx, idx1]