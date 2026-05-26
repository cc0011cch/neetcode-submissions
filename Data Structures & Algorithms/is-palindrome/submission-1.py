class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.lower()
        s2=''.join(c for c in s1 if c.isalnum())
        mid= len(s2)//2
        
        for i in range(mid):
            if s2[i]!=s2[-i-1]: return False
        return True