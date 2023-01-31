class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rows_2, cols_2 = rows - 2, cols - 2
        triples = [[sum(grid[r][c: c + 3]) for c in range(cols_2)]
                   for r in range(rows)]
        return max(triples[r][c] + triples[r + 2][c] + grid[r + 1][c + 1]
                   for r in range(rows_2) for c in range(cols_2))
