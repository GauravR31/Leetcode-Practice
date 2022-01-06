class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsSort = sorted(nums)
        resDict = {}
        for idx, val in enumerate(numsSort):
            if val not in resDict:
                resDict[val] = idx
                
        res = [resDict[val] for val in nums]
        
        return res