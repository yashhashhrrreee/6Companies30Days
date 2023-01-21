class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corner=set()
        c=lambda k:k[0]+k[1]
        a = lambda: (Y-y) * (X-x)
        area=0
        for x, y, X, Y in rectangles:
            area += a()
            corner ^= {(x, Y), (X, y), (x, y), (X, Y)}
    
        if len(corner) != 4:
            return False
        x, y = min(corner, key = c)
        X, Y = max(corner, key = c)
        return area == a()
        
 LEETCODE SUBMISSION LINK :https://leetcode.com/problems/perfect-rectangle/solutions/2988447/perfect-rectangle-solution/
