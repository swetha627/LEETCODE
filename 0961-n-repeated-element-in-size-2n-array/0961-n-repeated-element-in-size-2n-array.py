class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)//2
        d={}
        for i in nums:
            d[i]=d.get(i, 0)+1
        for k,v in d.items():
            if v==n:
                return k
        
        