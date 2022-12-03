class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d1=Counter(nums1)
        d2=Counter(nums2)
        ans1=[]
        ans2=[]
        for k,v in d1.items():
            if k not in d2:
                ans1.append(k)
        for k,v in d2.items():
            if k not in d1:
                ans2.append(k)
        return ans1, ans2
        
        
        