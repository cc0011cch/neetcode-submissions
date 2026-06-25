class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        b,c=1,0
        n=len(s)
        print('l:',n)
        for i in range(n-1,-1,-1):
            if s[i]=='0': a=0
            else: a=b
            if i+1<n and 10<=int(s[i:i+2])<=26:
                a+=c
            c=b
            b=a
        return b
  
        