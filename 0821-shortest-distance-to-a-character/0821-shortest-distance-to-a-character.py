class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        C=[]
        for i,v in enumerate(s):
            if v==c:
                C.append(i)
        res=[]
        for i in range(len(s)):
            res.append(min([abs(t-i) for t in C]))
        return res  
            
        
        
        