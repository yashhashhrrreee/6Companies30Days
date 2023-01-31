class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        dis = endPos - startPos
        if k-abs(dis) < 0 or (k-dis)%2 == 1:
            return 0
        if k-abs(dis) == 0:
            return 1
        if dis >= 0:
            left = self.getWays((k-dis)//2) 
            right = self.getWays((k-dis)//2 + dis)
        
        else:
            left = self.getWays((k+dis)//2 - dis)
            right = self.getWays((k+dis)//2)
        
        return (self.getWays(k) // (left*right)) % (10**9+7)
    
    def getWays(self, n):
        s = 1
        for i in range(1, n+1):
            s *= i
        print(s)
        return s
