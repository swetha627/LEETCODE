#https://leetcode.com/problems/product-of-array-except-self/description
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        pre=1
        for i in range(len(nums)):
            prefix[i]=pre
            pre=pre*nums[i]
        pos=1
        for i in range(len(nums)-1, -1, -1):
            postfix[i]=pos
            pos=pos*nums[i]
        for i in range(len(nums)):
            ans.append(prefix[i]*postfix[i])
        return ans
