class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']
        for i in tokens:
            if i not in operands:
                stack.append(i)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '+':
                    res = a + b
                elif i == '-':
                    res = a - b
                elif i == '*':
                    res = a * b
                else:
                    res = a / b
                stack.append(res)
        return int(stack[-1]) if stack else 0
                