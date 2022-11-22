class Solution:
    def freqAlphabets(self, s: str) -> str:
        d={}
        res=""
        ch=ord('a')
        for i in range(1,27):
            d[str(i)]=chr(ch)
            ch+=1
        i = 0
        res = ''
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#' :
                res += d[s[i:i+2]]
                i += 3
            else:
                res = res + d[s[i]]
                i += 1

        return res