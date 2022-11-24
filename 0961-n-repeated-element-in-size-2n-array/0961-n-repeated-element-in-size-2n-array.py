class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)//2
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
                if d[i]==n:
                    return i
            else:
                d[i]=1
        
        
        