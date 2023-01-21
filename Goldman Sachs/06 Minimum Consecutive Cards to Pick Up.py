class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        HashMap={}
        lengths=[]
        for i,j in enumerate(cards):
            if j in HashMap:
                lengths.append(abs(HashMap[j]-i)+1)
                HashMap[j]=i
            else:
                HashMap[j]=i
        if len(lengths)>0:
            return min(lengths)
        else:
            return -1``

 LEETCODE SUBMISSION LINK:https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/solutions/3073613/minimum-consecutive-cards-to-pick-up/
