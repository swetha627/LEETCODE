class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ch=ord('a')
        d=dict()
        for i in morse:
            d[chr(ch)]=i
            ch+=1
        s=set()
        for i in words:
            s.add(''.join([d[j] for j in i]))
        return len(s)
            
        