class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=dict()
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i], 0)+1
        for k,v in d.items():
            if v==1:
                return k

