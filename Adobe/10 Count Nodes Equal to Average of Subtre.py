class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        mi = float('inf')
        count = 0
        sum = 0

        for i in range(n):
            for j in range(n):
                mi = min(mi, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    count += 1
                sum += abs(matrix[i][j])
        if count % 2 == 0:
            return sum
        return sum - 2 * (mi)
