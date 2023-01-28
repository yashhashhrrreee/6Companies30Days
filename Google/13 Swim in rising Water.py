class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        queue = [(grid[0][0], 0, 0)]
        n = len(grid)
        visited = [[False]*n for i in range(n)]

        visited[0][0] = True

        ans = 0
        dirs = [0, 1,0,-1,0]
        while queue:

            curr = heappop(queue)
            if curr[0]>ans:
                ans = curr[0]
            if curr[1]==n-1 and curr[2]==n-1:
                return ans
            for i in range(4):
                next_i = curr[1] + dirs[i]
                next_j = curr[2] + dirs[i+1]

                if 0<=next_i<n and 0<=next_j<n and not visited[next_i][next_j]:
                    heappush(queue, (grid[next_i][next_j], next_i, next_j))
                    visited[next_i][next_j] = True


            
