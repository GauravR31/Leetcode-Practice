class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_map = {}
        
        for n in nums:
            count_map[n] = 0
        
        for n in nums:
            count_map[n] += 1
            if count_map[n] == 2:
                return True
            
        return False
            
        