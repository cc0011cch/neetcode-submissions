class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count=0

        def Palindrome(l,r):
            while l>=0 and r <len(s) and s[l]==s[r]:
                self.count+=1
                l-=1
                r+=1
            return

        for i in range(len(s)):
            l,r=i,i
            Palindrome(l,r)
            l,r=i,i+1
            Palindrome(l,r)

        return self.count
