class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans={}
        for i in set(nums):
            ans[i]=nums.count(i)
        for k,v in ans.items():
            if v>len(nums)//2:
                return k