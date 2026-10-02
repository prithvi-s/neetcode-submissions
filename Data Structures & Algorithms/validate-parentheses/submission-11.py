class Solution:
    def isValid(self, s: str) -> bool:
        d = { ')':'(' , '}':'{',  ']':'[' }
        stack = []
        top = -1
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            elif stack and d[i] == stack[top]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
            