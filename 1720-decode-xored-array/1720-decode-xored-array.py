class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = []
        arr.append(first)
        
        for i in range(len(encoded)):
            arr.append(encoded[i]^arr[i])
            
        return arr