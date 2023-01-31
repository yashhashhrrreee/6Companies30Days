class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        res={}
        total = -1
        for i in range(len(creators)):
            if creators[i] in res:
                res[creators[i]][0] += views[i]
                if res[creators[i]][2] < views[i]:
                    res[creators[i]][1] = ids[i]
                    res[creators[i]][2] = views[i]
                elif res[creators[i]][2] == views[i]:
                    res[creators[i]][1] = min(res[creators[i]][1],ids[i])
            else:
                res[creators[i]] = [views[i],ids[i],views[i]]
            total = max(res[creators[i]][0],total)
        
        result = []
        for i in res:
            if res[i][0] == total:
                result.append([i,res[i][1]])
        return result
