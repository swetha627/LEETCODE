class Solution:
    def replaceDigits(self, s: str) -> str:
        l=list(s)
        ans=[]
        for i in range(len(l)):
            if l[i].isalpha():
                ans.append(l[i])
                ch=ord(l[i])
            else:
                ans.append(chr(ch+int(l[i])))
        return ''.join(ans)
                
        