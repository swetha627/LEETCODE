class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        k=[i for i in nums if i%2==0]
        ans=list(k)
        j=[i for i in nums if i%2!=0]
        ans+=list(j)
        return ans