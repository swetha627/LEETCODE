class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        k=set(d.values())
        if len(d.values())==len(k):
            return True
        else:
            return False
                    