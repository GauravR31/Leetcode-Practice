class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for i in range(len(startTime)):
            if endTime[i] >= queryTime and startTime[i] <= queryTime:
                res += 1
                
        return res