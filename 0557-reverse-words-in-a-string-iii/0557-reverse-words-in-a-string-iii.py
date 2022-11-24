class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(" ")
        ans=[]
        for i in l:
            ans.append(i[::-1])
        return " ".join(ans)
        