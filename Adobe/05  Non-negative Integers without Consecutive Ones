class Solution:
	def findIntegers(self, num: int) -> int:
		solve = [0]* 32
		solve[0] = 1
		solve[1] = 2

		for i in range(2, 32):
			solve[i] = solve[i - 1] + solve[i - 2]

		i, add, prev = 30, 0, 0

		while i >= 0:
			if (num & (1 << i)) != 0:
				add += solve[i]
				if prev == 1:
					add -= 1
					break
				prev = 1
			else:
				prev = 0

			i -=1 

		return add + 1
    
