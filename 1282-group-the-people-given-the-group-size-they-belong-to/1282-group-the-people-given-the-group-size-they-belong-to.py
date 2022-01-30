class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {g:[] for g in groupSizes}
        
        for i,g in enumerate(groupSizes):
            groups[g].append(i)

        res = []
        
        for g in groups:
            group = groups[g]
            g_len = len(group)
            i = 0
            while i < g_len:
                res.append(group[i:i+g])
                i += g
                
        return res