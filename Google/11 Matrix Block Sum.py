class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        P = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + mat[i-1][j-1]
        def getSumOfRec(i1,j1,i2,j2):
            if i1<1:
                i1 = 1
            if j1<1:
                j1 = 1
            if i2>m:
                i2 = m
            if j2>n:
                j2 = n
            return P[i2][j2] - P[i1-1][j2] - P[i2][j1-1] + P[i1-1][j1-1]
        
        ans = [[0]*n for _ in range(m)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                ans[i-1][j-1] = getSumOfRec(i-k,j-k,i+k,j+k)
        return ans
