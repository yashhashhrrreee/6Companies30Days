class Solution:
    def peopleAwareOfSecret(self, n: int, Delay: int, Forget: int) -> int:

        canshare = 0
        delay = deque()
        forget = deque()
        day = 0

        delay.append([1+Delay,1])
        forget.append([1+Forget,1])
        while day <= n:
            if delay and delay[0][0] == day:
                canshare += delay.popleft()[1]
            if forget and forget[0][0] == day:
                canshare -= forget.popleft()[1]
            if canshare:
                delay.append([day+Delay,canshare])
                forget.append([day+Forget,canshare])

            day += 1
        
        while delay:
            canshare += delay.pop()[1]
        
        return canshare % (10**9+7)

