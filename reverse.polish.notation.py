class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stck=[]
        res = 0
        operators = ['+','-','*','/']
        import operator
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stck.append(tokens[i])
            if tokens[i] in operators:
                if len(stck) == 0:
                    return False
                num2 = stck.pop()
                num1 = stck.pop()
                res = int(ops[tokens[i]](int(num1), int(num2)))
                stck.append(res)
        return int(stck.pop())