class Solution:
    def isValid(self, s: str) -> bool:
        d = { ')' : '(', '}' : '{', ']' : '['}

        stack = []
        for i in s:
            if i in ['(' , '[', '{']:
                stack.append(i)
            elif stack and stack[-1] == d[i]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        return False
                
