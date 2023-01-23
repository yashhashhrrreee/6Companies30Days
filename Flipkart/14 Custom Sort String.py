 class Solution:
	def customSortString(self, order: str, s: str) -> str:
		if len(s) == 1:
			return s

		res = ''
		hash_s = collections.Counter(s)
		for char in order:
			if char in hash_s:
				res += char * hash_s[char]
				del hash_s[char]

		for key in hash_s:
			res += key * hash_s[key]  

		return res
