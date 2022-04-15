class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)+1):
            arr.append(i)
            
        return list(set(arr) - set(nums))[0]