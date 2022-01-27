class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        
        stack = []
        
        i = 0
        for c in list(s):
            if c == '(':
                i += 1
                if i > res:
                    res = i
                stack.append(c)
            elif c == ')':
                stack.pop()
                i -= 1
        
        return res