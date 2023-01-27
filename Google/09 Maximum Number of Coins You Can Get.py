class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        total = 0
        start = 1
        length = len(piles) //3
        while length != 0:
            total = total + piles[start]
            start+= 2
            length -= 1
        return total
