#https://leetcode.com/problems/longest-substring-without-repeating-characters/description
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # SLIDING WINDOW, TWO POINTERS
        maxLength=0
        charSet=set()
        l=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l]) # removing chareacters untill the duplicate
                l+=1
            charSet.add(s[r])
            maxLength=max(maxLength, r-l+1)
        return maxLength
