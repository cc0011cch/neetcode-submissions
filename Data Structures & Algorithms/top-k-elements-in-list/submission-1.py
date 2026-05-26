class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)
        freq=[[] for x in range(len(nums)+1)]
        for n,c in count.items():
           freq[c].append(n)
        rlt=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                rlt.append(n)
                if len(rlt)==k: return rlt
        return rlt
