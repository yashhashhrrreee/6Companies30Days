class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        dp = {(0, 0): (0, numArrows), (0, aliceArrows[1] + 1): (1, numArrows - (aliceArrows[1] + 1))}
        for i in range(2, 12):
            prev = dp
            dp = {}
            for key in prev:
                newkey1 = list(key)
                newkey1.append(0)
                score, arrowleft = prev[key]
                
                newval1 = (score, arrowleft)
                dp[tuple(newkey1)] = newval1
    
                if arrowleft >= aliceArrows[i] + 1:
                    newkey2 = list(key)
                    newkey2.append(aliceArrows[i] + 1)
                    newval2 = (score + i, arrowleft - (aliceArrows[i] + 1))
                    dp[tuple(newkey2)] = newval2
        maxscore, res = 0, None
        for key in dp:
            score, _ = dp[key]
            if score > maxscore:
                maxscore = score
                res = list(key)
        if sum(res) < numArrows:
            res[0] = numArrows - sum(res)
        
        return res

 LEETCODE SUBMISSION LINK:https://leetcode.com/problems/maximum-points-in-an-archery-competition/solutions/3073630/maximum-points-in-an-archery-competition/
