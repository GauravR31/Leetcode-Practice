class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stonesList = list(stones)
        jewelsList = list(jewels)
        res = 0
        for s in stonesList:
            if s in jewelsList:
                res += 1
                
        return res