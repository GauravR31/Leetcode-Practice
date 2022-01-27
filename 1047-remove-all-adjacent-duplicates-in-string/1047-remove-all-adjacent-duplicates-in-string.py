class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for c in list(s):
            if len(stack) != 0 and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
            
        return "".join(stack)
                