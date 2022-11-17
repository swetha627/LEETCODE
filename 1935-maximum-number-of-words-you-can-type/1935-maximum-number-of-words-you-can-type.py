class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        b=set(brokenLetters)
        for i in text.split():
            count+=all( c not in b for c in i)
        return count 
       
