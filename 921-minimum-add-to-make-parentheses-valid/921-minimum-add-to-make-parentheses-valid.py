class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        
        res = 0
        for c in list(s):
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    res += 1
                    
        stack_len = len(stack)
        return stack_len + res