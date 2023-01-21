class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcd_ans=numsDivide[0]
        for i in range(len(numsDivide)):
            gcd_ans=math.gcd(gcd_ans,numsDivide[i])
        nums.sort()
        count=0
        for i in nums:
            if gcd_ans%i==0:
                break
            else:
                count+=1
        if count==len(nums):
            return -1
        else:
            return count

LEETCODE SUBMISSION LINK: https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/solutions/3004229/minimum-deletions-to-make-array-divisible-solution/
