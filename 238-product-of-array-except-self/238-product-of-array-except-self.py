class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        
        left = 1
        right = 1
        for i in range(len(nums)):
            if i > 0:
                left = nums[i-1] * left
            pre[i] = left
            
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums) - 1:
                right = nums[i+1] * right
            suf[i] = right
        
        for i in range(len(nums)):
            answer.append(pre[i] * suf[i])
            
        return answer