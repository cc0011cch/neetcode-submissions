class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        longest=1
        length=1
        snums=sorted(set(nums))
        print(snums)
        for i in range(1,len(snums)):
            if snums[i]-snums[i-1]==1:
                length+=1
            else: length=1
            longest =max(longest,length)
        return longest
        