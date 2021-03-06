class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = -9999
        res = 0
        for r in rectangles:
            square_size = min(r)
            if square_size > maxLen:
                maxLen = square_size
                res = 1
            elif square_size == maxLen:
                res += 1
                        
        return res