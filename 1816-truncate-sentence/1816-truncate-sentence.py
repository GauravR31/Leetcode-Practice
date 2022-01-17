class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sentence_split = s.split(' ')
        
        return ' '.join(sentence_split[:k])