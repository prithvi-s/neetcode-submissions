class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = { 
            ')':'(',  ']':'[',  '}':'{' 
            }

        for i in s:
            if i not in d:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                elif stack[-1]!=d[i]:
                    return False
                else:
                    stack.pop()
        return len(stack)==0
                
                

