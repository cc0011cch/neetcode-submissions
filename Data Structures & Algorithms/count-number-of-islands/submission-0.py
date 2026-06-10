class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        islands=0

        def dfs(r,c):
            nonlocal area
            if r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]=='#'or grid[r][c]=='0': return
            area+=1
            grid[r][c]='#'
            dfs(r,c-1)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r+1,c)
            return
        for r in range(ROWS):
            for c in range(COLS):
                area=0
                dfs(r,c)
                if area>0: islands+=1
        return islands
