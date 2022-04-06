class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_vol = 0
        
        l = 0
        r = n-1
        
        while l < r:
            vol = (r-l) * min(height[l], height[r])
            max_vol = max(vol, max_vol)
            # print(l, r, height[l], height[r], vol, max_vol)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        
#         for i in range(l-1):
#             for j in range(i+1, l):
#                 vol = (j-i) * min(height[i], height[j])
#                 if vol > max_vol:
#                     max_vol = vol
#                     max_height = height[i]
#                     max_width = j-i

        return max_vol