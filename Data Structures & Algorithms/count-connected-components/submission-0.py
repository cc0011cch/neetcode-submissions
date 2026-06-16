class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        und_grap={i:[] for i in range(n)}
        for parent, child in edges:
            und_grap[parent].append(child)
            und_grap[child].append(parent)
        
        visit=[False]*n

        def dfs(node):
            for child in und_grap[node]:
                if not visit[child]:
                    visit[child]=True
                    dfs(child)

        no_of_connected=0
        for i in range(n):
            if not visit[i]:
                visit[i]=True
                dfs(i)
                no_of_connected+=1
        return no_of_connected

        