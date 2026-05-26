class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rs=''
        maxcount=0
        for c in s:
            if c not in rs:
                rs= rs+c
                maxcount=max(maxcount, len(rs))
            else:
                rs=rs[rs.index(c)+1:]+c

        return maxcount