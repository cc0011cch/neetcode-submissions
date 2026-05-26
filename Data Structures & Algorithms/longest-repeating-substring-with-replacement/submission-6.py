class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        winCount=defaultdict(int)
        maxFrq =0
        longest=0
        l=0
        for r in range(len(s)):
            winCount[s[r]]+=1
            maxFrq = max(winCount[s[r]],maxFrq)
            while r-l+1-maxFrq >k:
                   winCount[s[l]]-=1
                   l+=1
            longest=max(longest,r-l+1)
        return longest