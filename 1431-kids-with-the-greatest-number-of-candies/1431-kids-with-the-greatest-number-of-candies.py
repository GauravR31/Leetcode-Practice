class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)-extraCandies
        res = []
        
        for i in range(0, len(candies)):
            res.append((candies[i]) >= (maxCandies))
            
        return res
        