class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        arr = nums[:]
        arr.sort()
        
        lo, hi = 0, n - 1
        cnt = 0
        while lo <= hi and nums[lo] == arr[lo]:
            cnt += 1
            lo += 1
        
        while hi >= lo and nums[hi] == arr[hi]:
            cnt += 1
            hi -= 1
            
        return n - cnt
