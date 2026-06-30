class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)
        freq= dict(count.most_common())

        return list(freq.keys())[:k]
