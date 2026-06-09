from typing import List

class Tries:
    def __init__(self):
        self.children = {}
        self.EndofWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = Tries()
        def addDictionary(word: str):
            cur = self.root
            for c in word:
                if c not in cur.children: 
                    cur.children[c] = Tries()
                cur = cur.children[c]
            cur.EndofWord = True    

        for w in words:
            addDictionary(w)
            
        ROWS = len(board)
        COLS = len(board[0])
            
        def backtrack(r, c, node, word_str):
            # 1. 檢查邊界與字母
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == '#' or board[r][c] not in node.children: 
                return
            
            char = board[r][c]
            next_node = node.children[char]
            word_str = word_str + char # 直接在參數中傳遞新字串，連 nonlocal 都不需要
            
            # 2. 發現單字立刻加入結果集
            if next_node.EndofWord: 
                gp.add(word_str)
                # 【關鍵】這裡絕對不能 return！因為後面可能還有延伸的字（如 backend）

            # 3. 標記已造訪
            board[r][c] = '#'
            
            # 4. 繼續往四個方向探索
            backtrack(r-1, c, next_node, word_str)
            backtrack(r+1, c, next_node, word_str)
            backtrack(r, c-1, next_node, word_str)
            backtrack(r, c+1, next_node, word_str)
            
            # 5. 還原現場
            board[r][c] = char

        # 使用 set 避免不同路徑拼出同一個單字而重複加入
        gp = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                # 每次出發都傳入初始空字串 ''
                backtrack(r, c, self.root, '')
                
        return list(gp)
