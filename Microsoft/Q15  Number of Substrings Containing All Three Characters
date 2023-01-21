class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = {x: 0 for x in 'abc'}
        out, l = 0, 0
        
        for r in range(len(s)):
            counter[s[r]] += 1
            while all(counter.values()) > 0:
                out += len(s) - r
                counter[s[l]] -= 1
                l += 1
            
        return out
        
LEETCODE SUBMISSION LINK:https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/solutions/3073586/python-3-solution/
