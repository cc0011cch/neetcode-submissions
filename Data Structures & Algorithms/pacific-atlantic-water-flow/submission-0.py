class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #first find which set of locations fulfil requriment of pacific
    #2 find which set of  locations fulfil requriment of altantic
    #finally, result met both conditions.   
        pacific, atlantic = set(),set()
        ROWS=len(heights)
        COLS=len(heights[0])

        def dfs(r,c, visit, preHeight):
            if (r,c) in visit or r<0 or c<0 or r>=ROWS or c>=COLS or heights[r][c]<preHeight:
                return
            preHeight=heights[r][c]
            visit.add((r,c))
            dfs(r-1,c,visit, preHeight)
            dfs(r+1,c,visit, preHeight)
            dfs(r,c-1,visit, preHeight)
            dfs(r,c+1,visit, preHeight)
            return
            

        for c in range(COLS):
            dfs(0,c,pacific,heights[0][c])
            dfs(ROWS-1,c,atlantic,heights[ROWS-1][c])


        for r in range(ROWS):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,COLS-1,atlantic,heights[r][COLS-1])

        res=list()
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        return res





        