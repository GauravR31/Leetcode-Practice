class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        
        for idx, val in enumerate(nums):
            remain = target - val
            if remain in idx_map:
                return [idx_map[remain], idx]
            else:
                idx_map[val] = idx
                
        return -1,-1