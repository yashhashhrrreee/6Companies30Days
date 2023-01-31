class Solution:
    # Binary Search Approach
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)
        
        def ok(k):
            s = set(tuple(nums1[i : i + k]) for i in range(N - k + 1))
            return any(tuple(nums2[i : i + k]) in s for i in range(M - k + 1))
        l, r = 0, min(N, M)
        while l < r:
            m = (l + r + 1) // 2
            if ok(m): 
                # include m
                l = m
            else:
                # exclude m
                r = m - 1
        return l
