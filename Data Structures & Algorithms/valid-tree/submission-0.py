class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes={i:[] for i in range(n)}
        for parent, child in edges:
            nodes[parent].append(child)
            nodes[child].append(parent)


        visiting=set()
        def dfs(p, parent):
            if p in visiting: return False
            visiting.add(p)
            print(f"Visiting node: {p}, Current visited set: {visiting}")
            for c in nodes[p]:
                if c==parent: continue
                if not dfs(c,p): return False  
            return True


        if not dfs(0, -1): return False    
        return len(visiting) == n                
        