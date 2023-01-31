class Solution:
    def dp(self, nums):
        N = len(nums)
        dp = [(0, 0) for _ in range(N)]
        ans = 0
        
        for x in range(N):
            for y in range(x, N):
                if x == y:
                    dp[y] = (nums[y], nums[y])
                else:
                    dp[y] = (min(dp[y-1][0], nums[y]), dp[y-1][1] + nums[y])
                    a,b = dp[y]
                    ans = max(ans, a*b)
        
        return ans%(10**9+7)
    def minArray(self, nums):
        # Just to flush out the stack at the end of iterations.
        nums.append(0)
        
        N = len(nums)
        z = 0

        S = deque([[nums[0], 0]])
        
        rolling_sum = [0]*N
        rolling_sum[0] = nums[0]

        for idx in range(1, N):
            n = nums[idx]

            while S and S[-1][0] > n:                
                a,b = S.pop()
                
                if S:
                    b = S[-1][1]+1
                    z = max(z, rolling_sum[idx-1]*S[0][0])
                                    
                z = max(z, (rolling_sum[idx-1] - rolling_sum[b-1]) * a)

            S.append([nums[idx], idx])
            rolling_sum[idx] = n + rolling_sum[idx-1]
        return z%(10**9+7)
                
    def maxSumMinProduct(self, nums: List[int]) -> int:
        return self.minArray(nums)
