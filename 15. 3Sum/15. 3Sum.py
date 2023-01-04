#https://leetcode.com/problems/3sum/description

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TWO POINTERS
        ans=[]
        nums.sort()
        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l ,r =i+1, len(nums)-1
            while(l<r):
                threeSum=a+nums[l]+nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    ans.append([a,nums[l], nums[r]])
                    l+=1
                    while(l<r and nums[l]==nums[l-1]):
                        l+=1
        return ans

        #BRUTE FORCE
        # ans=[]
        # nums1=nums
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 if sorted([nums[i],nums[j],nums[k]]) not in ans:
        #                     ans.append(sorted([nums[i],nums[j],nums[k]]))
        # return ans
