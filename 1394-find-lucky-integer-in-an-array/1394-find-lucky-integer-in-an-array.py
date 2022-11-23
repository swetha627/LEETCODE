class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d=dict()
        
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        ans=[]
        for k,v in d.items():
            if k==v:
                ans.append(k)
        if ans:
            return max(ans)
        else:
            return -1


