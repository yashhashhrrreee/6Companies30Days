class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        prob = deque([1 if k <= pts <= n else 0 for pts in range(k, k + maxPts)])    
        cur_sum = sum(prob)
        for pts in range(k - 1, -1, -1):
            prob.appendleft(cur_sum / maxPts)
            cur_sum += prob[0] - prob.pop()
        return prob[0]
