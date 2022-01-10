class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        
        if num == 0:
            return steps
        
        while num != 1:
            if (num % 2) != 0:
                num = num-1
                steps += 1
            num = num / 2
            steps += 1
            
        return steps+1