class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s=sorted(nums)
        ans=0
        i=0
        while(i<len(nums)-1):
            ans+=min(s[i], s[i+1])
            i+=2
        return ans
            
            
        