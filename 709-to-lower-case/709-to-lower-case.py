class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        
        for c in s:
            if ord(c) >= 65 and ord(c) <= 90:
                res.append(chr(ord(c) + 32))
            else:
                res.append(c)
                
        return ''.join(res)