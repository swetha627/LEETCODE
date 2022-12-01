class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1=list(s1.split(" "))
        l2=list(s2.split(" "))
        ans=[]
        for i in l1:
            if i not in l2 and l1.count(i)==1:
                ans.append(i)
        for i in l2:
            if i not in l1 and l2.count(i)==1:
                ans.append(i)
        return ans
                
        