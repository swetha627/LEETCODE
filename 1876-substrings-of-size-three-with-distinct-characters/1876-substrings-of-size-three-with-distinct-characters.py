class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)-2):
            temp=""
            for j in range(i, i+3):
                if s[j] not in temp:
                    temp+=s[j]
                if len(temp)==3:
                    count+=1
        return count
                