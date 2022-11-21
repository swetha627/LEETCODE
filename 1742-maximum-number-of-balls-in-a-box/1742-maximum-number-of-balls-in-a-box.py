class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d=dict()
        for i in range(lowLimit, highLimit+1):
            s=str(i)
            res=0
            for i in s:
                res+=int(i)
            d[res]=d.get(res, 0)+1
        return max(d.values())

    
    
        