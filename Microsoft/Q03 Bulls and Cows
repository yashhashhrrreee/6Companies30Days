class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cow_indices = [0 for _ in range(10)]
        cows = 0
        bulls = 0
        length = len(secret)
        for i in range(length):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s = int(secret[i])
                g = int(guess[i])
                if cow_indices[s] < 0:
                    cows += 1
                cow_indices[s] += 1
                if cow_indices[g] > 0:
                    cows += 1
                cow_indices[g] -= 1
        return "%dA%dB" % (bulls,cows)
        
        LEETCODE SUBMISSION LINK :https://leetcode.com/problems/bulls-and-cows/solutions/2988327/bulls-and-cows-solution/
