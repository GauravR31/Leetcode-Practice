class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            resCount = 0
            for j in range(len(nums)):
                if nums[j] < nums[i] and j != i:
                    resCount += 1
            res.append(resCount)
            
        return res