class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)
        freq= count.most_common()
        print(freq)
#        freq=[[] for _ in range(len(nums)+1)]
        
#        for n,c in count.items():
#           freq[c].append(n)
        output=[]
        for key,c in freq:
            output.append(key)
            if len(output)==k: return output
#        for i in range(len(freq)-1,0,-1):
#            for n in freq[i]:
#                output.append(n)
#                if len(output)==k: return output
