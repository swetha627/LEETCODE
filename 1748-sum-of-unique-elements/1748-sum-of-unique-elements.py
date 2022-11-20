class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d=dict()
        for i in nums:
            d[i]=d.get(i, 0)+1
        sum=0
        for k,v in d.items():
            if v==1:
                sum+=k
        return sum
            
        