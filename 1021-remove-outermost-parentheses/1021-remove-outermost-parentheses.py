class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        start_idx = 0
        end_idx = 0
        
        stack = []
        i = 0
        
        res = ""
        
        for c in list(s):
            if c == '(':
                stack.append(c)
                i += 1
            elif c == ')':
                stack.pop()
                i += 1
                
                if len(stack) == 0:
                    start_idx = end_idx
                    end_idx = i
                    
                    res += s[start_idx+1:end_idx-1]
                    
        return res