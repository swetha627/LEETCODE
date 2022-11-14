class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        else:
            s1,s2=max(strs), min(strs)
            i=0
            while i<len(s1) and i<len(s2) and s1[i]==s2[i]:
                i=i+1
            return s1[0:i]
            
            
            
                
       
            
            
        