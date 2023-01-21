class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = list(sorted([p1, p2, p3, p4]))
        def line(a, b):
            return points[b][0] - points[a][0], points[b][1] - points[a][1]
        length = lambda line: math.sqrt(line[0]**2 + line[1]**2)
        
        l, b, t, r = line(0, 1), line(0, 2), line(3, 1), line(3, 2)
        sides = length(t) == length(b) == length(t) == length(r) > 0
        angles = l[0] * b[0] + l[1] * b[1] == t[0] * r[0] + t[1] * r[1] == 0
        return sides and angles

LEETCODE SUBMISSION LINK: https://leetcode.com/problems/valid-square/solutions/3073595/valid-square/
