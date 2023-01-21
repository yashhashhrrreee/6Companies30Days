class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashTree = {}
        for x,y in prerequisites:
            if x not in hashTree:
                hashTree[x] = []
            if y not in hashTree:
                hashTree[y] = []
            hashTree[x].append(y)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if node not in hashTree or len(hashTree[node]) == 0:
                return True
            
            visited.add(node)
            for pre in hashTree[node]:
                if not dfs(pre):
                    return False
            visited.remove(node)
            hashTree[node] = []
            return True

        for c in range(numCourses):
            if c not in hashTree or len(hashTree[c]) == 0:
                continue
            if not dfs(c):
                return False
        return True
        
        LEETCODE SUBMISSION LINK:https://leetcode.com/problems/course-schedule/solutions/2988477/course-scheduling-solution/
