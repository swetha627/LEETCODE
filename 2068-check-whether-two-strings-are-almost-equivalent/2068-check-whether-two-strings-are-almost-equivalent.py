class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d1={}
        d2={}
        for i in word1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in word2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        for i in word1+word2:
            if i in d1 and i in d2:
                if abs(d1[i]-d2[i])>3:
                    return False
            elif (i in d1 and d1[i]>3) or (i in d2 and d2[i]>3):
                return False
        return True