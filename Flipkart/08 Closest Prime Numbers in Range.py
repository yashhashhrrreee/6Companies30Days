class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n):
            if n<2:
                return False

            for x in range(2,int(n**0.5)+1):
                if n%x==0:
                    return False

            return True

        q=[]
        diff=float('inf')
        pair=[-1,-1]
        for i in range(left,right+1):
            if isPrime(i):
                q.append(i)

            while len(q)>=2:
                if abs(q[0]-q[1])<diff:
                    pair=[q[0],q[-1]]
                    diff=abs(q[0]-q[1])
                    if diff<=2:
                        return pair

                q.pop(0)

        return pair                                
