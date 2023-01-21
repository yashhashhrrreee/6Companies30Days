class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n > second:
                return True

            if n > first:
                second = min(n, second)

            else:
                first = min(n, first)

        return False
