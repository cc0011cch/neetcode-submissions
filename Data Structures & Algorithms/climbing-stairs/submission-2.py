class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,2
        rlt=0
        if n<=2: return n
        for _ in range(n-2):
            rlt=a+b
            a, b = b,rlt
        return rlt
        