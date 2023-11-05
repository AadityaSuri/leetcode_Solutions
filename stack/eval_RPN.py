import math
class Solution:
    def op_result(self, num1, num2, op):
        match op:
            case '+':
                return num1 + num2
            case '-':
                return num1 - num2
            case '*':
                return num1 * num2
            case '/':
                ret = num1 / num2
                if ret < 0:
                    return math.ceil(ret)
                else:
                    return math.floor(ret)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = set(('+', '-', '*', '/'))
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                ret = self.op_result(num1, num2, token)
                stack.append(ret)

        return stack[-1]