class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d=dict()
        ans=list()
        for i in range(len(names)):
            d[heights[i]]=names[i]
        for i in sorted(d.keys(),reverse=True):
            ans.append(d[i])
        return ans
        
            