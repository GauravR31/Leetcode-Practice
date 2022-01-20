class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split(' ')
        res = []
        
        for w in s_split:
            res.append(w[::-1])
            
        return ' '.join(res)