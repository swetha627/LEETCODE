#https://leetcode.com/problems/permutation-in-string/description
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1=Counter(s1)
        for i in range((len(s2)-len(s1))+1):
            d2=Counter(s2[i:i+len(s1)])
            if d1==d2:
                return True
            else:
                d2={}
        else:
            return False
