class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def isValid(s):
            if not s or int(s) > 255 or (s[0] == '0' and s != "0"):
                return False
            return True

        if len(s) < 4 or len(s) > 16:
            return []
        ans = []
        for i in range(1,4):
            for j in range(i+1,i+5):
                for k in range(j+1,j+5):
                    first, second, third, last = s[0:i], s[i:j], s[j:k], s[k:]
                    if isValid(first) and isValid(second) and isValid(third) and isValid(last):
                        ans.append(first + '.' + second + '.' + third + '.' + last)
        return ans
