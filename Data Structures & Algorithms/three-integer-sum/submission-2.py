class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums=sorted(nums)
        rlt=[]
        print(snums)
        for i, num1 in enumerate(snums[:-2]):
            for j,num2 in enumerate(snums[i+1:-1]):
                if -num1-num2 in snums[i+j+2:]:
                    tmp = sorted([num1, num2,-num1-num2])
                    if  tmp not in rlt:
                        rlt.append(tmp)
        return rlt
