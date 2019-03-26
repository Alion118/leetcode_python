import collections
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = collections.defaultdict(list)
        for u,v in prerequisites:
            g[v].append(u)
        visited=[0]*numCourses
        def dfs(i):
            if visited[i]==1:return False
            if visited[i]==2:return True
            visited[i]=1
            for j in g[i]:
                if not dfs(j):return False
            visited[i]=2
            return True
        for i in range(numCourses):
            if not dfs(i):return False
        return True

print(Solution().canFinish(2,[[1,0]]))