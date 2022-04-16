class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        w = [0] * (n)
        w[0] = 1
        w[1] = 2
        
        print(w)
        
        for i in range(2, n):
            w[i] = w[i-1] + w[i-2]
            
        print(w)
        return w[n-1]
        