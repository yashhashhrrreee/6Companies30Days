class Solution:
    def binmatch(self,A,k):
        i,s = 0,0
        for i,x in enumerate(A):
            s += x
            if s>=k:
                s -= x
                break
        return i,s
    def bincount(self,n,r):
        A = [0]*r
        s = 1
        while n>0:
            for i in range(r):
                s     = min(n,s)
                A[i] += s
                n    -= s
                if n<=0:
                    break
            s *= 10
        return A  
    def remainder(self,t,c): # target, container size
        if t==1:
            return # t=1 is always Null Zero (1,10,100,etc..)
        t -= 1 # subtract Null Zero
        c -= 1
        A  = self.bincount(c,r=10)
        i,s = self.binmatch(A,t)
        yield i
		# yield from self.remainder(t-s,A[i]) # only works in Python 3
        for j in self.remainder(t-s,A[i]): 
            yield j
    def findKthNumber(self, n, k): #-> int:
        # Find first digit:
        A   = self.bincount(n,r=9)
        i,s = self.binmatch(A,k)
        res = i+1
        # Find Upcoming Digits
        for x in self.remainder(k-s,A[i]):
            res = 10*res + x
        return res
