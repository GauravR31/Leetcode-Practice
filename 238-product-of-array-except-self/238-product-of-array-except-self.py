class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        
        left = 1
        right = 1
        for i in range(len(nums)):
            if i > 0:
                left = nums[i-1] * left
            answer[i] = left
            
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums) - 1:
                right = nums[i+1] * right
            answer[i] *= right
            
        return answer