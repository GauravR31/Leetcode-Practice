class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res_dict = {}
        
        for i in range(len(queries)):
            res_dict[i] = 0
            
        for p in points:
            for i,q in enumerate(queries):
                if ((q[0]-p[0])**2 + (q[1]-p[1])**2)**0.5 <= q[2]:
                    res_dict[i] += 1
            
        res = []
        for q in res_dict.keys():
            res.append(res_dict[q])
            
        return res