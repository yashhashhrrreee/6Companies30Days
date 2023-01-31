class TweetCounts:
    def __init__(self):
        self.T = defaultdict(list)
        self.delta = {'minute':60, 'hour': 3600, 'day':24*3600}
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.T[tweetName],time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:   
        j = -1
        out = []
        for t in list(range(startTime-1,endTime,self.delta[freq]))+[endTime]:
            k = bisect.bisect(self.T[tweetName],t)
            if j>=0: out.append(k-j)
            j=k
        return out
