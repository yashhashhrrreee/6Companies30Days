class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # radix
        R = 26
        
        def char_to_int(ch: chr) -> int:
            return ord(ch) - ord('a')
        
        # preprocessng
        recent_ind = [len(s)] * R
        next_char = [()] * len(s) # next_char[i][j] gives next ind of char j after an index i
        
        for i in range(len(s) - 1, -1, -1):
            next_char[i] = tuple(recent_ind) # R operations
            recent_ind[char_to_int(s[i])] = i
        
        # processing
        res = 0
        for word in words: # loop through words
            cur = recent_ind[char_to_int(word[0])] # start at first letter
            for i in range(1, len(word)): # find if next_char exists for all chars in word
                if not cur < len(s):
                    break
                cur = next_char[cur][char_to_int(word[i])] # go to index of next char
            
            if cur < len(s): # if next char exists for all chars, add 1 to answer
                res += 1
        
        return res
