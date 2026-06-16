class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        und_grap={i:[] for i in range(n)}
        for parent, child in edges:
            und_grap[parent].append(child)
            und_grap[child].append(parent)
        
        visit=set()

        def dfs(node):
            visit.add(node)
            for child in und_grap[node]:
                if child not in visit:
                    dfs(child)

        no_of_connected=0
        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                no_of_connected+=1
        return no_of_connected

        