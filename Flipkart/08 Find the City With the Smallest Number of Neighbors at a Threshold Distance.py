class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]

        for origin, destination, weight in edges:
            dist[origin][destination] = weight
            dist[destination][origin] = weight

        

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        
        ans = 0
        exceed = n - 1
        for i in range(n):
            validCities = 0
            for j in range(n):
                if i == j:
                    continue
                if dist[i][j] <= distanceThreshold:
                    validCities += 1

            if validCities <= exceed:
                ans = i
                exceed = validCities

        return ans

        

        
