class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        longest=1
        snums=set(nums)
        for num in snums:
            if num-1 in nums:
                length=2;
                n=num-2
                while n in nums:
                    length+=1
                    n-=1

                if longest< length:
                    longest=length
        return longest
        