class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d={}
        ch=ord('a')
        for i in distance:
            d[chr(ch)]=i
            ch+=1
        sl=set()
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i]==s[j] and d[s[i]]==(j-i)-1:
                    sl.add(s[i])
        if sl==set(s):
            return True
        else:
            return False
                
        