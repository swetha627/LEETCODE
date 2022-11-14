class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.rstrip()
        list1=l.split()
        i=len(list1)
        res=len(list1[i-1])
        return res
       
                
        