class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        if len(nums) == 0:
            return res
        
        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i]:
                diff = nums[i] - nums[i+1] + 1
                nums[i+1] += diff
                res += diff
                
        return res