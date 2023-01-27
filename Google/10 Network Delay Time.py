from heapq import *
class Solution:
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for source,dest,weight in times:
            graph[source].append([dest,weight])
        time = {}
        heap = []
        heappush(heap, [0,K])
        # in heap put distance as key otherwise wont sort it 
        
        while heap:
            dist, node = heappop(heap)
            if node not in time:
                time[node] = dist
                for child, wei in graph[node]:
                    if child not in time:
                        heappush(heap,[wei+dist,child])
        return max(time.values()) if len(time) == N else -1
        
        
