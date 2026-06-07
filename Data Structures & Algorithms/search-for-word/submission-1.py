class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        def dfx(r,c,Index):
            if Index==len(word): return True
            if r<0 or c<0 or r>=m or c>=n or board[r][c]!=word[Index] or board[r][c]=='#':
                return False
            board[r][c]='#'
            res = dfx(r+1,c,Index+1) or dfx(r-1,c,Index+1) or dfx(r,c+1,Index+1) or dfx(r,c-1,Index+1)
            board[r][c] = word[Index]
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):       
               if dfx(r,c,0): return True
        return False