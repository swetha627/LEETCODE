class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d=dict()
        for i in range(len(paths)):
            d[paths[i][0]]=paths[i][1]
        k=list(d.keys())
        v=list(d.values())
        for i in v:
            if i not in k:
                return i
