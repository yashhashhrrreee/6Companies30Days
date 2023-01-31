class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """
        # OPTIMAL Approach
        # create wordMap = {a: [a, acd, ace], b: [bb] ...}
        # on each iter it becomes {a:[], b: [b], c: [cd, ce] ...} and small
        # Time Complexity: O(n) + O(m)  
        """
        
        count = 0
        wordMap = defaultdict(list)
        
        for w in words:
            wordMap[w[0]].append(w)
            
        for c in s:
            wordList = wordMap[c]
            wordMap[c] = []
            
            for w in wordList:
                if len(w) == 1:
                    count += 1
                else:
                    wordMap[w[1]].append(w[1:])
                    
                    
        return count
                    
        
        
        """
        # Brute Force 2 (ACCEPTED)
        # Time Complexity: O(kn) + O(m) (Approx. O(kn))
        # Where, k = num of unique subseq in words, m = len(words)
		# n = len(s)
        """
        count = 0
        seqInWords = {}
        
        for seq in words:
            seqInWords[seq] = 1 + seqInWords.get(seq, 0)
            
        for seq in seqInWords:
            n = len(seq)
            i = 0
            
            for c in s:
                if i == n: break
                if c == seq[i]: i += 1
                    
            if i == n: count += seqInWords[seq]
                
        return count
        
        
        
        """
        # brute force 1
        """
        
        count = 0
        for seq in words:
            n = len(seq)
            i = 0
            idx = -1
            for x in range(len(seq)):
                c = seq[x]
                ind = idx+1
                while ind < len(s):
                    if c == s[ind]:
                        idx = ind
                        i += 1
                        break
                        
                    ind += 1
                    
            if i == n: count += 1
                    
        return count
                    
