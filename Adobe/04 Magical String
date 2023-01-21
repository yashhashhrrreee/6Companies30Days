class Solution:
    def magicalString(self, n: int) -> int:
        s = ['1', '2', '2']
        for i in range(2, n):
            add_two = s[-1] == '1'
            s.extend(list(int(s[i]) * ('2' if add_two else '1')))
            if len(s) >= n: break 
        return s[:n].count('1')
