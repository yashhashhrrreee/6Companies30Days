class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        R, C = len(dungeon), len(dungeon[0])
        memo = [[-1] * C for _ in range(R)]

        def dp(i, j):
            #base
            if i >= R or j >= C:
                return float(inf)
            if i == R - 1 and j == C - 1:
                memo[-1][-1] = 1 - dungeon[-1][-1] if dungeon[-1][-1] < 0 else 1
            
            #check memo
            if memo[i][j] != -1:
                return memo[i][j]
            
            #recursive define
            ret = min(dp(i + 1, j), dp(i, j + 1)) - dungeon[i][j]
            memo[i][j] = ret if ret > 0 else 1
            return memo[i][j]

        return dp(0, 0)
