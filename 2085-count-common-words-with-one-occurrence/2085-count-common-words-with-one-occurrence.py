class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1={}
        d2={}
        count=0
        for i in words1:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for j in words2:
            if j not in d2:
                d2[j]=1
            else:
                d2[j]+=1
        for k in d1:
            if k in d2:
                if d1[k]==1 and d2[k]==1:
                    count+=1
        return count
                
        