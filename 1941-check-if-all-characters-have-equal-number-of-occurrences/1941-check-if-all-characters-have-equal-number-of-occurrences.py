class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d=dict()
        for i in range(len(s)):
            d[s[i]]=d.get(s[i], 0)+1
        t=set(d.values())
        if len(t)==1:
            return True
        else:
            return False
