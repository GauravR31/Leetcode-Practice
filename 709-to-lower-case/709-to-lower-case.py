class Solution:
    def toLowerCase(self, s: str) -> str:
        charList = list(s)
        
        for i in range(len(charList)):
            if ord(charList[i]) >= 65 and ord(charList[i]) <= 90:
                charList[i] = chr(ord(charList[i]) + 32)
                
        return ''.join(charList)