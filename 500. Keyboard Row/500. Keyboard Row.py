#https://leetcode.com/problems/keyboard-row/description
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans=[]
        d={}
        for i in "qwertyuiop":
            d[i]=1
        for j in "asdfghjkl":
            d[j]=2
        for k in "zxcvbnm":
            d[k]=3
        for i in words:
            if len(i)==1:
                ans.append(i)
            else:
                i_lower=i.lower()
                same=True
                for j in range(len(i)-1):
                    if d[i_lower[j]]!=d[i_lower[j+1]]:
                        same=False
                        break
                if same:
                    ans.append(i)
        return ans
