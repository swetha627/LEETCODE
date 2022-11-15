class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        previous_ele=1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[previous_ele]=nums[i]
                previous_ele+=1
        return previous_ele
        
        
        