class Solution:
    def isValid(self, s: str) -> bool:
        ref= {'(':')', '[':']', '{':'}'}
        
        basket=[]
        for c in s:
            if c in ref:
                basket.append(ref[c])
            else:
                if len(basket)==0: return False
                if c != basket.pop():
                    return False
        
        if len(basket)==0: return True
        else: return False