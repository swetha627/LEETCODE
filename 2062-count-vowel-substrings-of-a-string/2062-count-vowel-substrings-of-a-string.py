class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowel=set("aeiou")
        count=0
        for i in range(len(word)):
            s=set()
            if(word[i] in vowel):
                for j in range(i,len(word)):
                    if(word[j] in vowel):
                        s.add(word[j])
                    
                        if(s==vowel):
                            count+=1
                    else:
                        break
        return count
        