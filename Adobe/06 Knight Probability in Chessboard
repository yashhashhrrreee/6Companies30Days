class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        # Generates all 8 moves
        total_moves = {(i, j) for i in {-2, -1, 1, 2} for j in {-2, -1, 1, 2} - {i} - {-i}}
              
        # A dictionary to store (K, r, c) for DP
        mmap = {}
        
        def dp(K, r, c, cur_prob = 1):
            if K == 0:
                # If there are no more moves left, then store the probability landing on that 
                # square, then return the value
                mmap[(K, r, c)] = cur_prob
                return cur_prob
            else:
                # Generates all possible moves originating from the current square
                pos_moves = {(r + dr, c + dc) for dr, dc in total_moves \
                                                    if 0 <= r + dr < N and 0 <= c + dc < N}
                res = 0
                for dr, dc in pos_moves:
                    if (K - 1, dr, dc) in mmap:
                        # If the dict already has the probability for that square, 
                        # then we don't need to recurse
                        res += mmap[(K - 1, dr, dc)]
                    else:
                        # If we had NOT calculated the probability, we recurse into 
                        # next possible moves, with each move being 1/8th as probable
                        res += dp(K - 1, dr, dc, cur_prob / 8)
                    
                mmap[(K, r, c)] = res
                return res
            
        return dp(K, r, c)
