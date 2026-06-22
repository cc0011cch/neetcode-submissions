class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res, self.reslen =0,0
        def Palindromic(left,right):
                while left>=0 and right<len(s) and s[left]==s[right]:
                    if right-left+1 >self.reslen:
                        self.reslen=right-left+1
                        self.res=left
                    left-=1
                    right+=1
                return 

        for idx in range(len(s)):
            l,r =idx,idx
            Palindromic(l,r)
            l,r =idx, idx+1
            Palindromic(l,r)

        return s[self.res:self.res+self.reslen]