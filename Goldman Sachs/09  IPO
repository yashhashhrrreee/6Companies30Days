import heapq as hq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        tasks = list(zip(capital, profits))
        tasks.sort(key=lambda x: x[0])
        
        t, t_count = 0, len(tasks)
        q = []
        
        for _ in range(k):
            while t < t_count and tasks[t][0] <= w:
                hq.heappush(q, -tasks[t][1])
                t+=1
            
            if q:
                w -= hq.heappop(q)
            else:
                break
        
        return w
