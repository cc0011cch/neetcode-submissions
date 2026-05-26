class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            tlst=list(t)
            for s_c in s:
                for tidx,t in enumerate(tlst):
                 if s_c is t:
                       tlst.pop(tidx)
                       break
            if len(tlst)==0: 
                return True
            else: 
                return False
        return False