class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d=dict()
        ch=''
        for i in range(len(s)):
            d[s[i]]=d.get(s[i], 0)+1
            if d[s[i]]==2:
                ch=s[i]
                break
        return ch
