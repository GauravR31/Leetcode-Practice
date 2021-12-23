class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        l = len(nums)
        total = 0
        
        for i in range(l):
            total += nums[i]
            runningSum.append(total)
            
        return runningSum
