class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        minn=[]
        maxx=[]
        res=[]
        for i in matrix:
            minn.append(min(i))
        for j in range(n):
            ans=0
            for k in range(m):
                if matrix[k][j]>ans:
                    ans=matrix[k][j]
            maxx.append(ans)
        for i in maxx:
            if i in minn:
                res.append(i)
        return res
            
        