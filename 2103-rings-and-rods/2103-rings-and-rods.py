class Solution:
    def countPoints(self, rings: str) -> int:
        d=dict()
        c=[]
        di=[]
        for i in range(len(rings)):
            if rings[i].isalpha():
                c.append(rings[i])
            else:
                di.append(rings[i])
        for i in range(len(c)):
            d[di[i]]=d.get(di[i], "")+c[i]
        count=0
        for i in d.values():
            if set(i)==set('BGR'):
                count+=1

        return count
        