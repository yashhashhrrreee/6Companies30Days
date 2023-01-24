class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        mx=0
        special=sorted(special)
        for i in range(1,len(special)):
            mx=max(special[i]-special[i-1],mx)
        return max(mx-1,special[0]-bottom,top-special[-1])
