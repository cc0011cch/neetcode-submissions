class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b,c,d=0,0,0,0
 #       if len(nums)==1: return nums[0]
 #       for idx, n in enumerate(nums):
 #           if idx < len(nums)-1:
 #               a,b = b, max(b,n+a)
 #           if idx >0:
 #               c,d = d, max(d,c+n)
 #       return max(b,d)
        def rob_select(n:List[int])->int:
            a,b=0,0
            for num in n:
#                a,b = b, max(b,num+a)
                temp = b
                b=max(b,num+a)
                a=temp
            return b
            
        return max(nums[0],rob_select(nums[:-1]),rob_select(nums[1:]))
        