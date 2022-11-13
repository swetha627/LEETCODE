class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res=""
        index=0
        size=len(word)
        for i in range(len(word)):
            if word[i]==ch:
                index=i
                break
        count=index
        while index>-1:
            res+=word[index]
            index-=1
        res=res+word[count+1:]
        return res


        