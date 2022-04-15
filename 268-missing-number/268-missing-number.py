class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        for i in nums:
            res += i
    
        print((n*(n+1)/2))
        print(res)
        return int((n*(n+1)/2) - res)