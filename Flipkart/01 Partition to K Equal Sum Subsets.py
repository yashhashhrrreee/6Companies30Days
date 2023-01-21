class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        if k > n:
            return False

        total = 0
        for num in nums:
            total += num 

        if total % k != 0:
            return False  
        subTotal = total / k 

        nums.sort(reverse=True)
        used = ['0' for _ in range(n)]
        memo = {}
        return self.backtrack(nums, 0, 0, k, used, subTotal, memo)
    
    def backtrack(self, nums, start, bucket, k, used, target, memo):
        if k == 0:
            return True 
        
        usedStr = ''.join(used)

        if bucket == target:
            res = self.backtrack(nums, 0, 0, k - 1, used, target, memo)
            memo[usedStr] = res
            return res
        
        if usedStr in memo:
            return memo[usedStr]

        for i in range(start, len(nums)):
            if used[i] == '1':
                continue 
            
            if bucket + nums[i] > target:
                continue 
            
            bucket += nums[i]
            used[i] = '1' 
            if self.backtrack(nums, i + 1, bucket, k, used, target, memo):
                return True 
            used[i] = '0' 
            bucket -= nums[i]

        return False 
