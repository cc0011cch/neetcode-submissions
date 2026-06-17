class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        universe=set()
        for word in words:
            universe = universe.union(set(word))
#        print(universe)
# use dict as graph to build relationships between words
#
#        graph={item:"" for item in universe}
# need to use set as "j","abcdefghi","jk","k"]=> j=>a and j=>k.. using char will lost a.
        graph={item:set() for item in universe}
        for i in range(len(words)-1):
            l_a,l_b = len(words[i]),len(words[i+1])
            if l_a>l_b and words[i][:l_b]==words[i+1]: return ""
            m_len = l_a
            if l_a>l_b: m_len=l_b
            for j in range(m_len):
                if words[i][j]!=words[i+1][j]: 
                    graph[words[i][j]].add(words[i+1][j])
                    # use break because we only need to hit the recent char amd ignore remains
                    break

        print(graph)
        # use dfs to find solution..by focusing on finding child is empty.. then copy the parent, 
        #remove the node and then use the content of parent to find the child and make it to empty..then dfs.. till to empy graph.
        visit={} #use for cycle detection
        rlt=[]
        def dfs(char):
            if char in visit: return visit[char]    
            visit[char] = True        
             # 1. Get the child character
            for child in graph[char]: # 遍历所有合法子节点
                if dfs(child): # it will back to line 29 "if char in visit: return visit[char]"
                    return True # 发现环，一路向上无损传递 True 信号

            visit[char] = False   
            rlt.append(char)      
            return False         

        for g in graph:
            if dfs(g): return ""
        print(rlt)
        rlt.reverse()
        print("".join(rlt))
        res ="".join(rlt)
        return res

