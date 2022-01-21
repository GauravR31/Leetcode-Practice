class Solution:
    def minPartitions(self, n: str) -> int:
        n_split = list(n)
        
        n_int = map(int, n)
        
        return max(n_int)