class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = len(words)
        for word in words:
            for w in word:
                if w not in set(allowed):
                    consistent -= 1
                    break
        
        return consistent