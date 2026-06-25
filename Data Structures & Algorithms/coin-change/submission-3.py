class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem={}
        def dfs(remain:int):
            if remain == 0: return 0
            if remain in mem: return mem[remain]
            res=1e9
            for coin in coins:
                if remain-coin>=0:
                    res = min(res, 1 + dfs(remain-coin))
            mem[remain]=res
            return res
        mcoin=dfs(amount)
        return -1 if mcoin>=1e9 else mcoin  
        
        