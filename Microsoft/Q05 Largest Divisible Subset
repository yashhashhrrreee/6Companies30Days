class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        nums.sort()
        
        dp = [[num] for num in nums]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        
        max_len = 0
        res = []
        for subset in dp:
            if len(subset) > max_len:
                max_len = len(subset)
                res = subset

        return res

LEETCODE SUBMISSION LINK:https://leetcode.com/problems/largest-divisible-subset/solutions/2988429/largest-divisible-subset-solution/
