class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        mx = [0]
        def dfs(ansset, remain):
            nonlocal mx
            if remain == "":
                if len(ansset) >= mx[0]:
                    mx[0] = len(ansset)
            for i in range(len(remain)+1):
                insert = remain[:i]
                if insert not in ansset and insert != '':
                    ansset.add(insert)
                    dfs(ansset, remain[i:])
                    ansset.remove(insert)
        
        dfs(set({}),s)
        return(mx[0])
