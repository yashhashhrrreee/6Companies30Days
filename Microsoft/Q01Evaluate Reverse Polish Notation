class Solution:
    def evalRPN(self, tokens) -> int:
        if (len(tokens) == 1):
            return int(tokens[0])

        stack = []
        top = -1
        operators = "+-*/"

        for ele in tokens:
            if (ele in operators):
                rhs = int(stack.pop())
                lhs = int(stack.pop())
                res = 0
                if (ele == "+"):
                    res = lhs+rhs
                elif (ele == "-"):
                    res = lhs-rhs
                elif (ele == "*"):
                    res = lhs*rhs
                elif (ele == "/"):
                    res = int(lhs/rhs)
                stack.append(res)
            else:
                top += 1
                stack.append(ele)
        
        return stack[0]


lEETCODE SUBMISSION LINK:https://leetcode.com/problems/evaluate-reverse-polish-notation/solutions/2983622/evaluate-reverse-polish-notation-solution/
