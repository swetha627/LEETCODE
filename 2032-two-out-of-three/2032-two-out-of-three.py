class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    ans.append(i)
                for k in nums3:
                    if k==i or j==k:
                        ans.append(k)
        return set(ans)
            
                    
        