class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq={i:[] for i in range(numCourses)}

        for cur_crs, pre_crs in prerequisites:
            preReq[cur_crs].append(pre_crs)

        visiting =set()
        def dfs(cur_crs):
            if cur_crs in visiting: return False
            if preReq[cur_crs] == []: return True

            visiting.add(cur_crs)
            for p in preReq[cur_crs]:
              if not dfs(p): return False

            visiting.remove(cur_crs)
            preReq[cur_crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):return False
        return True


        