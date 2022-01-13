class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        
        for c in s:
            cOrd = ord(c)
            if cOrd >= 65 and cOrd <= 90:
                res.append(chr(cOrd + 32))
            else:
                res.append(c)
                
        return ''.join(res)