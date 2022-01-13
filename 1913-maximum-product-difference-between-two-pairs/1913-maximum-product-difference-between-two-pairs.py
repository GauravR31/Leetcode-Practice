class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maxNum = max(nums)
        minNum = min(nums)
        
        nums.remove(maxNum)
        maxNum2 = max(nums)
        
        nums.remove(minNum)
        minNum2 = min(nums)
        
        return (maxNum * maxNum2) - (minNum * minNum2)