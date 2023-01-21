class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        queue = collections.deque([[n, n, n] for n in nums]) 
        for i in range(1, len(nums)):
            queue[i][1] = max(queue[i-1][1], nums[i])
        
        for i in range(len(nums)-2, -1, -1):
            queue[i][2] = min(queue[i+1][2], nums[i])
            
        while queue and queue[0][1] == queue[0][2]:
            queue.popleft()
        
        while queue and queue[-1][1] == queue[-1][2]:
            queue.pop()
                
        return len(queue)
            
 LEETCODE SUBMISSION LINK:https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solutions/3004086/shortest-unsorted-continuous-subarray-solution/
