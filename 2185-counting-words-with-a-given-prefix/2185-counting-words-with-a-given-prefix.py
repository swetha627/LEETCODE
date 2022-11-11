class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans=0
        for i in words:
            if pref==i[0:len(pref)]:
                ans+=1
        return ans
        
        