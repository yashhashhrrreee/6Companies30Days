class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        self.ans = 0
		# good candidate set for O(1) lookup
        good = set()
        
        def backtracking(idx, count):
            if idx == n:
				# found a potential solution
                self.ans = max(self.ans, count)
                return
            
            # assume idx is good
            good.add(idx)
            for i in range(idx):
				# check for any contradictions with previous assumptions
                if (statements[idx][i] == 1 and i not in good) or (statements[idx][i] == 0 and i in good) or (i in good and statements[i][idx] == 0):
                    break
            else:
				# if no contradiction found then we can assume idx is good and continue search
                backtracking(idx + 1, count + 1)
            good.remove(idx)
            
            # assume idx is bad
            for i in range(idx):
				# check for any contradictions with previous candidates thought to be good
                if (i in good and statements[i][idx] == 1):
					# contradiction so prune current branch
                    return
            backtracking(idx + 1, count)
    
        backtracking(0, 0)
        return self.ans
