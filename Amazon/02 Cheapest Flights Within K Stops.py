class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for source, destination, cost in flights:
            graph[source].append((cost, destination))
        
        q = []
        seen = set()
        heappush(q,(0,src,0))

        while len(q) != 0:
            price, current, steps = heappop(q)
            if (current, steps) in seen or steps > k+1:
                continue
            if current == dst:
                return price
            seen.add((current, steps))
            for child in graph[current]:
                heappush(q, (child[0]+price, child[1], steps+1))
        return -1
