class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        ans = 0
        n = len(nums1)
        nums = [nums1[i] - nums2[i] for i in range(n)]
        vis = []
        for i in range(n - 1, -1, -1):
            if not vis:
                vis.append(nums[i] + diff)
            else:
                pos = bisect.bisect_left(vis, nums[i])
                ans += len(vis) - pos
                bisect.insort(vis, nums[i] + diff)
        return ans
        
LEETOCDE SUBMISSION LINK :https://leetcode.com/problems/number-of-pairs-satisfying-inequality/solutions/3004062/number-of-pairs-satisfying-inequality-solution/
