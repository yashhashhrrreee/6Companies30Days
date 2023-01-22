class Solution:
    def findTheCity(self, n: int,
                    edges: List[List[int]],
                    distanceThreshold: int) -> int:
        g = defaultdict(list)
        for a,b,w in edges:
            g[a].append( (b,w) )
            g[b].append( (a,w) )

        def hlpr(city: int) -> int:
            h = [(0, city)]
            seen = set()

            while h:
                net_cost, city = heapq.heappop(h)
                if city in seen: continue
                seen.add(city)

                for path, fee in g[city]:
                    if path not in seen and net_cost + fee <= distanceThreshold:
                        heapq.heappush(h, (net_cost + fee, path))
            return len(seen) - 1

        min_reach, res = float("inf"), None
        for i in range(n):
            tmp = hlpr(i)
            if tmp <= min_reach:
                min_reach = tmp
                res = i
        return res

	def findTheCity1(self, n: int,
                    edges: List[List[int]],
                    distanceThreshold: int) -> int:
        g = defaultdict(dict)
        for a,b,w in edges:
            g[a][b] = w
            g[b][a] = w

        def hlpr(city: int, funds: int, seen: Set) -> None:
            if funds == 0: return

            for path in g[city]:
                if path not in seen and g[city][path] <= funds:
                    hlpr(path, funds - g[city][path], seen | set([city]))
                    visit.add(path)

        min_reach, res = float("inf"), None
        for i in range(n):
            visit = set()
            hlpr(i, distanceThreshold, set())

            if len(visit) <= min_reach:
                min_reach = len(visit)
                res = i
        return res
