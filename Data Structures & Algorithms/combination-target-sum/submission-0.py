class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        rlt=list()
        nums.sort()
        def dfs(start,path,total):
            if total==target:
                rlt.append(path.copy())
                return
            for j in range(start,len(nums)):
                if total+nums[j] > target:
                    return
                path.append(nums[j])
                
                dfs(j, path, total+nums[j])
                path.pop()

        dfs(0,[],0)
        return rlt
