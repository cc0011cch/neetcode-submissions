from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: 
                return mid
            if nums[mid] > nums[r]: #代表「左半邊」是正常遞增排序的
                # 步驟 2：檢查 target 是否在左半邊正常區間內
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # 步驟 3：在左邊，把右指針拉過來
                else:
                    l = mid + 1  # 不在左邊，去右邊找
            else:
                # 步驟 2：檢查 target 是否在右半邊正常區間內
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # 步驟 3：在右邊，把左指針拉過去
                else:
                    r = mid - 1  # 不在右邊，去左邊找


        return -1
