class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #build histogram for nums
        count= Counter(nums)
        #sort the value of histogram in decending order
        # use dict because output is list(tuple)
        freq= dict(count.most_common())

        return list(freq.keys())[:k]
