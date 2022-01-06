class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        resList = list(s).copy()
        sIter = 0
        
        for i in indices:
            resList[i] = s[sIter]
            sIter += 1
            
        return ''.join(resList)
        