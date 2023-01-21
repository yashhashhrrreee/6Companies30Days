class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        neg = False
        if numerator * denominator < 0:
            neg = True
        numerator, denominator = abs(numerator), abs(denominator)
        inte = numerator // denominator
        numerator %= denominator
        deci = []
        vis = {}
        idx = 0
        flag = False
        while numerator:
            numerator *= 10
            while numerator < denominator:
                numerator *= 10
                deci.append('0')
                idx += 1
            if numerator in vis:
                flag = True
                break
            vis[numerator] = idx
            deci.append(str(numerator // denominator))
            idx += 1
            numerator %= denominator

        if not deci:
            return ("-" if neg else "") + str(inte)
        if flag:
            return ("-" if neg else "") + str(inte) + '.' + "".join(deci[:vis[numerator]]) + '(' + "".join(deci[vis[numerator]:]) + ')'
        return ("-" if neg else "") + str(inte) + '.' + "".join(deci)
