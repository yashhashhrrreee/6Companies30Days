class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        BIT = [0] * (N+1)
        nums = [0] * N
        num1 = [0] * N
        num2 = [0] * N
        for i, n in enumerate(nums1):
            num1[n]=i
        for i, n in enumerate(nums2):
            num2[n]=i
        for i, n in enumerate(num1):
            nums[n] = num2[i]
        def lowbit(i):
            return i&(-i)
        def add(i):
            i+=1
            while i <= N:
                BIT[i]+=1
                i+=lowbit(i)
        def query(i):
            i += 1
            re = 0
            while i:
                re += BIT[i]
                i -= lowbit(i)
            return re
        smaller = []
        bigger = []
        for i, n in enumerate(nums):
            smaller.append(query(n))
            bigger.append(N-1-i-n+smaller[-1])
            add(n)
        return sum(i*j for i, j in zip(smaller, bigger))
	
 LEETCODE SUBMISSION LINK:https://leetcode.com/problems/count-good-triplets-in-an-array/solutions/3073621/count-good-triplets-in-an-array/
