import math 

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            gain = int(str(num)[::-1]) - num
            if not (gain in d):
                d[gain] = 1 
            else:
                d[gain] += 1 
        num_of_nice_pairs = 0 
        for gain in d:
            n = d[gain] 
            if n >= 2:
                num_of_nice_pairs +=  math.comb(n, 2)
                
        return num_of_nice_pairs % (10**9 + 7)
