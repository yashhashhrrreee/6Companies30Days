class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


        if len(points) <= 2:
            return 0

        ans = 0

        hashtable =  {}
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    dis = distance(points[i], points[j])
                    if dis in hashtable:
                        hashtable[dis] += 1
                    else:
                        hashtable[dis] = 1

            # print(hashtable)
            
            for d in hashtable:
                if hashtable[d] > 1:
                    ans += hashtable[d] * (hashtable[d] - 1)
            
            hashtable = {}



        return ans

        
        
LEETCODE SUBMISSION LINK:https://leetcode.com/problems/number-of-boomerangs/solutions/3073606/number-of-boomerangs/
