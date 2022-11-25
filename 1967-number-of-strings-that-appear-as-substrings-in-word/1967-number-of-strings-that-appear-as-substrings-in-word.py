class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans=[]
        for i in patterns:
            if i in word:
                ans.append(i)
        return len(ans)