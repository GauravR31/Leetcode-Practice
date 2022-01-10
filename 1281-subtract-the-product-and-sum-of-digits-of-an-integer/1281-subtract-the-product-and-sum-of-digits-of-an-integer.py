class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nString = list(str(n))
        prod = 1
        add = 0
        
        for s in nString:
            x = int(s)
            prod = prod * x
            add += x
            
        return prod - add