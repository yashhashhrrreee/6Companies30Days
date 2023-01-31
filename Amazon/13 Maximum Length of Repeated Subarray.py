class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        finalDict = {}
        
        for word in words:
            if word in finalDict.keys():
                finalDict[word] +=1
            else:
                finalDict[word] = 1
        finalList = []
        cnt = 0
        for key,val in sorted(finalDict.items(),key=lambda x:(-x[1],x[0])):
            if cnt < k:
                finalList.append(key)
            cnt +=1
        return finalList
