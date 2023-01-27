class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        res = 0
        seen = set()
        
        for i in range(n):
            divisible = 0
            for j in range(i,n):
                divisible+=1 if nums[j]%p == 0 else 0
                
                if divisible > k:
                    break
                    
                subarray = tuple(nums[i:j+1])
                if subarray in seen:
                    continue
                
                seen.add(subarray)
                res+=1
                
        return res
