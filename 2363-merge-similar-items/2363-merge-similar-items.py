class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d1,d2={},{}
        for i in items1:
            d1[i[0]]=i[1]
        for i in items2:
            d2[i[0]]=i[1]
        res=[]
        k=list(d1.keys())
        k+=list(d2.keys())
        for i in set(k):
            if i in d1 and i in d2:
                li=list([[i, d1[i]+d2[i]]])
                res.extend(li)
            elif i in d1 and i not in d2:
                res.extend([[i, d1[i]]])
            else:
                res.extend([[i, d2[i]]])
        
        return sorted(res)


