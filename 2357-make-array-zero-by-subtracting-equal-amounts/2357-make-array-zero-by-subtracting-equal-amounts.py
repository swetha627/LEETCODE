class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        if 0 in d.keys():
            return len(d.keys())-1
        else:
            return len(d.keys())
            
            