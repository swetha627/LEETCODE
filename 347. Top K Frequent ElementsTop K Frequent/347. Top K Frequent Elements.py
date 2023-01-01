#https://leetcode.com/problems/top-k-frequent-elements/description
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=sorted(d.items(), key=lambda x:x[1],reverse=True)
        d2=dict(l)
        for i in d2.keys():
            if k>0:
                ans.append(i)
                k-=1
        return ans
