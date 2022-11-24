class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if nums[j]!=nums[i]:
                    for k in range(j+1, len(nums)):
                        if nums[k]!=nums[j] and nums[k]!=nums[i]:
                            count+=1
        return count
        