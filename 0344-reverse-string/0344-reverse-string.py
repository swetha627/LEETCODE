class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lower=0
        higher=len(s)-1
        for i in range(len(s)//2):
            s[lower], s[higher]=s[higher], s[lower]
            lower+=1
            higher-=1
        return s
        
        