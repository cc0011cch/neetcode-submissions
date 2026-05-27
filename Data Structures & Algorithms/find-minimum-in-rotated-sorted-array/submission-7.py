class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        l=0
        r=len(nums)-1 
        if len(nums)==2: 
            if nums[l]<nums[r]: return nums[l]
            else: return nums[r]        
        mid=0
        while l<r:
            mid = (r+l)//2
            print(l,mid,r)    
            if (r-l+1)%2:
                if nums[mid]-nums[l]>nums[r]-nums[mid]:
                    l=mid
                else: r=mid
            else:
                if nums[mid]-nums[l]>nums[r]-nums[mid+1]:
                    l=mid+1 
                else:
                    r=mid
            print(l,r)
            if l==r: return nums[l]    
            if r-l==1:
                if nums[l] < nums[r]:
                    return nums[l]
                else: return nums[r]
