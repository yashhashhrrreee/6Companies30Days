class Solution:

    def __init__(self, w: List[int]):
        s = 0
        self.weight = []        
        for weight in w:
            s += weight
            self.weight.append(s)                    
            
    def pickIndex(self) -> int:
        return bisect_left(self.weight, random.randint(1, self.weight[-1]))

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
