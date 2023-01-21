class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        total = sum(A)
        ans = cur = sum(i * n for i, n in enumerate(A))
        for i in range(len(A)-1, 0, -1):
            cur += total - len(A) * A[i]
            ans = max(ans, cur)
        return ans
        
        LEETCODE SUBMISSION LINK:https://leetcode.com/problems/rotate-function/solutions/2988380/rotate-function-solution/
