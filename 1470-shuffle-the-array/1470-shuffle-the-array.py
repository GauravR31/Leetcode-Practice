class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:len(nums)//2]
        y = nums[len(nums)//2:]
        
        res = []
        
        for i in range(len(x)):
            res.append(x[i])
            res.append(y[i])
            
        return res