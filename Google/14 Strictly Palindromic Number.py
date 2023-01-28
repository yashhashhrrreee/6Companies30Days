class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            a=n
            s=""
            while(a>0):
                s+=str(a%i)
                a=int(a/i)
            if(s!=s[::-1]):
                return False
        return True
